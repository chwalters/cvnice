import json
import os
import tempfile
from datetime import date
from typing import Optional

from carbone_sdk import carbone_sdk
from email_validator import validate_email, EmailNotValidError
from glom import glom
from nicegui import app, ui, events, run
from pydantic import TypeAdapter, AnyUrl, ValidationError
from supabase import Client as SupabaseClient
from loguru import logger

from config import settings, Settings
from model import resume_cv
from model.application import AppModel
from model.resume_cv import Iso8601
from services.analytics import PosthogAnalytics
from services.basic_lingua.blingua_sdk_python.src.blinguasdk import BlinguaSDK
from services.basic_lingua.blingua_sdk_python.src.blinguasdk.models import errors
from services.database.supa import get_client


class Editor:

    editor_sections = dict(
        basics=dict(
            title="Basics",
            prop="basics",
            icon="person",
            tab_index=0,
        ),
        work=dict(
            title="Work",
            prop="work",
            icon="work",
            tab_index=1,
        ),
        volunteer=dict(
            title="Volunteering",
            prop="volunteer",
            icon="volunteer_activism",
            tab_index=2,
        ),
        education=dict(
            title="Education",
            prop="education",
            icon="school",
            tab_index=3,
        ),
        awards=dict(
            title="Awards",
            prop="awards",
            icon="military_tech",
            tab_index=4,
        ),
        certificates=dict(
            title="Certification",
            prop="certificates",
            icon="redeem",
            tab_index=5,
        ),
        publications=dict(
            title="Publications",
            prop="publications",
            icon="description",
            tab_index=6,
        ),
        skills=dict(
            title="Skills",
            prop="skills",
            icon="local_activity",
            tab_index=7,
        ),
        languages=dict(
            title="Languages",
            prop="languages",
            icon="language",
            tab_index=8,
        ),
        interests=dict(
            title="Interests",
            prop="interests",
            icon="interests",
            tab_index=9,
        ),
        references=dict(
            title="References",
            prop="references",
            icon="people",
            tab_index=10,
        ),
        project=dict(
            title="Projects",
            prop="projects",
            icon="account_tree",
            tab_index=11,
        )
    )

    def add_item_at_index(self, app_model: AppModel, target, prop, path, index, cv_schema, cv,
                          supabase: SupabaseClient):
        prop_name = prop.split(".")[-1]
        try:
            target_type = type(target)
            field_info = target_type.__fields__[prop_name]
            target_attr_type = field_info.annotation.__args__[0].__args__[0]
            new_prop_value = target_attr_type()
            target_attr = getattr(target, prop_name)
            if target_attr is None:
                target_attr = []
                setattr(target, prop_name, target_attr)
            target_attr.append(new_prop_value)
            self.save_model(app_model, cv, supabase)
            # editor_content.refresh()
        except Exception as e:
            print(e)

    async def delete_item_at_index(
            self, app_model: AppModel, root_model, target, prop, path, index, cv_schema, cv,
            supabase: SupabaseClient
    ):
        prop_name = prop.split(".")[-1]
        if "items" in prop_name:
            prop_name = prop.split(".")[-2]

        with ui.dialog() as confirmation_dialog, ui.card():
            ui.label(f"Are you sure you want to delete this section or item in '{prop_name}'?")
            with ui.row().classes('w-full justify-center'):
                ui.button('Yes, delete it', color="positive", icon="delete",
                          on_click=lambda: confirmation_dialog.submit(True))
                ui.button('No', on_click=lambda: confirmation_dialog.submit(False))

        result = await confirmation_dialog
        if result is True:
            delete_target = getattr(root_model, prop_name)
            if delete_target and len(delete_target) >= index:
                delete_target.remove(delete_target[index])
                self.save_model(app_model, cv, supabase)

    def property_field(
            self,
            app_model: AppModel,
            parent_path: str,
            prop: str,
            bind_target,
            model_item: resume_cv.Resume,
            cv_schema: dict,
            cv: resume_cv.Resume,
            supabase: SupabaseClient
    ):
        if prop is not None:
            type: Optional[str] = glom(cv_schema, f'{parent_path}.properties.{prop}.type', default=None)
            ref: Optional[str] = glom(cv_schema, f'{parent_path}.properties.{prop}.$ref', default=None)
            format: Optional[str] = glom(cv_schema, f'{parent_path}.properties.{prop}.format', default=None)

            if bind_target is not None:
                bind_value_target = bind_target
            else:
                bind_value_target = glom(model_item, f"{parent_path.replace('properties.', '')}", default=None)
                if bind_value_target is None:
                    bind_value_target = model_item

            if type is None or type == "string":
                if ref is not None and "iso8601" in ref:
                    with ui.input(prop.title()).bind_value(
                        bind_value_target,
                        prop,
                        backward=lambda sd: self.iso8601_to_datetime(sd),
                        forward=lambda dt: self.datetime_to_iso8601(dt)
                    ) as dfield:
                        with ui.menu():
                            ui.date().bind_value(
                                dfield
                            )
                        with dfield.add_slot('prepend'):
                            ui.icon('edit_calendar')
                else:
                    if "summary" in prop or "reference" in prop:
                        async def summarize(text_area: ui.textarea, settings_obj: Settings):
                            try:
                                s = BlinguaSDK()
                                res = await run.io_bound(
                                    s.text_summarize_wrapper_text_summarize_summary_length_post,
                                    summary_length="short",
                                    request_body=text_area.value.encode("utf-8"),
                                    api_key=settings_obj.gemini_api_key
                                )
                                if res.text_result is not None:
                                    text_area.value = res.text_result.results
                                else:
                                    pass
                            except errors.SDKError as e:
                                pass

                        with ui.textarea("Summary").bind_value(bind_value_target, prop) as text_area:
                            with ui.context_menu():
                                ui.menu_item('Summarize..', on_click=lambda: summarize(text_area, settings))
                    else:
                        type_prop = ""

                        def validate_emailinput(v):
                            ret_val = None
                            if v is not None and len(v) > 0:
                                try:
                                    validate_email(v)
                                    ret_val = None
                                except EmailNotValidError:
                                    ret_val = "Invalid email"
                            return ret_val
                        def validate_url(v):
                            retVal = None
                            if v is not None and len(v) > 0:
                                try:
                                    AnyUrl(v)
                                    retVal = None
                                except:
                                    retVal = "Invalid URL"
                            return retVal

                        if format is not None and "uri" in format:
                            validation_lambda = validate_url
                            forward_lambda = lambda u: u
                            backward_lambda = lambda u: str(u) if u is not None else None
                            type_prop='type="url"'
                        elif format is not None and "email" in format:
                            validation_lambda = validate_emailinput
                            forward_lambda = lambda u: u
                            backward_lambda = lambda u: str(u) if u is not None else None
                            type_prop = 'type="email"'
                        else:
                            validation_lambda = lambda u: None
                            forward_lambda = lambda u: str(u)
                            backward_lambda = lambda u: str(u)

                        with ui.input(prop.title(), validation=validation_lambda).bind_value(
                            bind_value_target,
                            prop,
                            backward=backward_lambda,
                            forward=forward_lambda
                        ).props(
                            'bottom-slots ' + type_prop
                        ) as f:
                            field_description = glom(
                                cv_schema,
                                f'{parent_path}.properties.{prop}.description',
                                default=None
                            )
                            if field_description is not None:
                                with f.add_slot('hint'):
                                    ui.label(field_description)
            elif type == "array":
                with ui.card().classes("w-full").props("flat bordered").tight() as item_card:
                    with ui.row().classes('w-full'):
                        ui.label(f"{prop.title()}")
                        ui.button(
                            f"Add {prop.title()}",
                            icon="add",
                            on_click=lambda: self.add_item_at_index(app_model, bind_value_target, prop, parent_path, 0, cv_schema, cv, supabase)
                        ).props(
                            'flat outlined size=s color=positive'
                        )
                    array_items = glom(bind_value_target, prop, default=[])
                    if array_items is not None and len(array_items) > 0:
                        item_index: int = 0
                        inputs = []
                        delete_input_buttons = []
                        for item in array_items:
                            with ui.card_section().classes('w-full'):
                                item_path = f"{parent_path}.properties.{prop}.items"
                                sub_props = glom(cv_schema, f"{item_path}.properties", default=[])
                                if sub_props is not None and len(sub_props) > 0:
                                    for sub_prop in sub_props:
                                        self.property_field(app_model, item_path, sub_prop, item, bind_value_target, cv_schema, cv, supabase)
                                    ui.button(
                                        f"Delete {prop.title()}",
                                        icon="add",
                                        # app_model, root_model, target, prop, path, index, cv_schema, cv, supabase)
                                        on_click=lambda i=item_index: self.delete_item_at_index(
                                            app_model, bind_value_target, bind_value_target, prop, item_path, i, cv_schema, cv, supabase)
                                    ).props('flat outlined size=s color=negative')


                                else:
                                    def set_item(target, prop, input_array, e):
                                        value = e.value
                                        target_index = input_array.index(e.sender)
                                        if target_index != -1:
                                            array_items[target_index] = value
                                        setattr(target, prop, array_items)
                                        # property_field.refresh()
                                    def delete_item(target, prop, input_array, e):
                                        target_index = input_array.index(e.sender)
                                        if target_index != -1:
                                            array_items.remove(array_items[target_index])
                                        setattr(target, prop, array_items)
                                        self.save_model(app_model, cv, supabase)

                                    with ui.input(
                                            "Item",
                                            value=item,
                                            on_change=lambda e: set_item(bind_value_target, prop, inputs, e)
                                    ) as array_item_input:
                                        inputs.append(array_item_input)
                                        with array_item_input.add_slot("prepend"):
                                            with ui.button(
                                                icon="delete",
                                                on_click=lambda e: delete_item(bind_value_target, prop, delete_input_buttons, e)
                                            ).props('flat outlined size=s color=negative') as delete_input_button:
                                                delete_input_buttons.append(delete_input_button)
                                        with array_item_input.add_slot("append"):
                                            ui.button(
                                                icon="add",
                                                on_click=lambda: self.add_item_at_index(app_model, bind_value_target, prop, parent_path,
                                                                                   item_index, cv_schema, cv, supabase)
                                            ).props('flat outlined size=xs color=positive')
                            item_index = item_index + 1

            elif type == "object":
                with ui.card().classes("w-full").props("flat bordered").tight():
                    ui.label(f"{prop.title()}")
                    item = glom(bind_value_target, prop, default={})
                    with ui.card_section().classes('w-full'):
                        item_path = f"{parent_path}.properties.{prop}"
                        sub_props = glom(cv_schema, f"{item_path}.properties", default=[])
                        if sub_props is not None and len(sub_props) > 0:
                            for sub_prop in sub_props:
                                self.property_field(app_model,item_path, sub_prop, item, bind_value_target, cv_schema, cv, supabase)
                        else:
                            ui.input("Item", value=item).bind_value(bind_value_target, item)
            else:
                logger.warning(f"Unsupported type: {type}")

    def save_model(
        self,
        app_model: AppModel,
        cv_model: resume_cv.Resume,
        supabase: SupabaseClient
    ):
        if cv_model is not None:
            json_model = cv_model.model_dump_json()
            if json_model is not None:
                user_id = app.storage.user.get("user_id", None)
                if user_id is not None:
                    data, count = supabase.table('personae').update({
                        'owner': user_id,
                        'cv_resume': json_model
                    }).eq('owner', user_id).execute()
                    logger.debug(f"Saved to supabase: {data} {count}")
        self.editor_content.refresh(app_model)


    @ui.refreshable
    def property_editor(
            self,
            app_model: AppModel,
            parent_path: str,
            model_item: resume_cv.Resume,
            cv_schema: dict,
            property_name: str,
            title: str,
            delete_title: str,
            idx: int,
            root_model: resume_cv.Resume,
            cv: resume_cv.Resume,
            supabase: SupabaseClient
    ):
        ui.label(title).classes("text-h4")
        path = f'{parent_path}'
        type = glom(cv_schema, f"{path}.type", default=None)
        if type is not None:
            if "object" in type:
                with ui.card().classes('w-full q-ma-md').props('flat bordered').tight() as card:
                    with ui.card_section().classes('w-full q-pa-md') as section:
                        ui.badge(f"Section #{idx+1}")
                        for prop in glom(cv_schema, f"{path}.properties", default=[]):
                            self.property_field(app_model,path, prop, None, model_item, cv_schema, cv, supabase)
                    if "Basics" not in title:
                        section_title = delete_title
                        with ui.card_actions().classes('w-full'):
                            ui.button(
                                f"Delete {section_title} Section #{idx+1}",
                                icon="delete",
                                on_click=lambda: self.delete_item_at_index(app_model, root_model, model_item, path, path, idx, cv_schema, cv, supabase)
                            ).props('flat outlined size=s color=negative')
            elif "array" in type:
                with ui.row().classes('w-full'):
                    ui.button(
                        f"Add {title}",
                        icon="add",
                        on_click=lambda: self.add_item_at_index(app_model, model_item, path, path,
                                                           0, cv_schema, cv, supabase)
                    ).props('flat outlined size=s color=positive')
                array_items = glom(model_item, property_name, default=None)
                if array_items is not None and len(array_items) > 0:
                    item_index = 0
                    for item in array_items:
                        self.property_editor(app_model,f"{path}.items", item, cv_schema, property_name, "", title, item_index, root_model, cv, supabase)

                        item_index = item_index + 1


    def iso8601_to_datetime(self,thing: Iso8601):
        if isinstance(thing, Iso8601):
            dt = date.fromisoformat(thing.model_dump())
        else:
            dt = thing
        return dt

    def datetime_to_iso8601(self, thing):
        is8601 = None
        if isinstance(thing, date):
            is8601 = Iso8601(root=str(thing.isoformat()))
        else:
            if thing is not None:
                try:
                    is8601 = Iso8601(root=thing)
                except:
                    pass
        return is8601

    current_tab = 'Basics'
    current_editor = 'Form View'

    async def open_json_cv(self, app_model: AppModel, supabase: SupabaseClient):
        with ui.dialog() as open_dialog:
            async def load_cv(e: events.UploadEventArguments):
                cv_json = e.content.read().decode("utf-8")
                try:
                    acv = TypeAdapter(resume_cv.Resume).validate_json(cv_json)
                    if acv:
                        app_model.personae[0].cv_resume = acv
                        self.save_model(app_model, acv, supabase)
                except ValidationError as ve:
                    with ui.dialog() as error_dialog:
                        with ui.card().classes('w-full'):
                            ui.label("Parse/Validation Errors").classes("text-negative")
                            ui.textarea(value=str(ve)).classes('w-full')
                            with ui.card_actions().classes('w-full justify-end'):
                                ui.button('Close', on_click=error_dialog.close)
                    result = await error_dialog
                finally:
                    open_dialog.close()

            ui.upload(on_upload=load_cv).classes('w-full')

            await open_dialog


    def json_editor_content(self, app_model: AppModel, supabase: SupabaseClient):
        cv = app_model.personae[0].cv_resume
        cv_json = cv.model_dump_json()
        cv_json_with_str = json.loads(cv_json)
        def save_json_to_model(new_content):
            try:
                acv = TypeAdapter(resume_cv.Resume).validate_json(json.dumps(new_content.get('json', None)))
                if acv:
                    if acv is not None:
                        app_model.personae[0].cv_resume = acv
                        self.save_model(app_model, acv, supabase)
            except Exception as ve:
                ui.notify(str(ve), color="negative")

        ui.json_editor({'content': {'json': cv_json_with_str}},
                       on_change=lambda e: save_json_to_model(e.content)).style("--jse-theme-color: #0F588C;")

    def tab_content(self, section, tabs, app_model, cv, cv_schema, supabase: SupabaseClient):

        self.property_editor(
            app_model,
            f"properties.{section['prop']}",
            cv,
            cv_schema,
            section['prop'],
            section['title'],
            section['title'],
            0,
            cv,
            cv,
            supabase
        )

    @ui.refreshable
    async def editor_content(self, app_model: AppModel, analytics: Optional[PosthogAnalytics] = None):
        cv_schema: dict = json.loads(open("model/schema/jsoncv_schema.json").read())
        cv = app_model.personae[0].cv_resume # resume_cv.Resume = TypeAdapter(resume_cv.Resume).validate_json(json_example)

        user_id = app.storage.user.get("user_id", None)
        if user_id is not None:
            username = app.storage.user.get("username", None)
            if username is not None:
                supabase: SupabaseClient = get_client(username)
                if supabase is not None:
                    my_auth = supabase.auth.get_session().user.id
                    response = supabase.table('personae').select('cv_resume').eq('owner', user_id).execute()
                    if response is not None:
                        if len(response.data) > 0:
                            cv = TypeAdapter(resume_cv.Resume).validate_json(
                                response.data[0]['cv_resume'])
                            app_model.personae[0].cv_resume = cv
                        else:
                            logger.warning('Zero personae loaded')
                            app.storage.user.clear()
                    else:
                        logger.warning('No personae found')
                        app.storage.user.clear()
                else:
                    logger.warning('No user_id to fetch personae for user')
                    app.storage.user.clear()
                    supabase: SupabaseClient = get_client("username")

        global current_tab
        global current_editor


        def tab_changed(e):
            app_model.settings.last_tab = e.value
            app.storage.user['editor_last_tab'] = app_model.settings.last_tab

        def editor_changed(e):
            app_model.settings.last_editor = e.value
            app.storage.user['editor_last_editor'] = app_model.settings.last_editor

        def splitter_changed(e):
            app_model.settings.last_splitter = e.value
            app.storage.user['editor_last_splitter'] = app_model.settings.last_splitter

        async def export_pdf(
                app_model: AppModel,
                cv_model: resume_cv.Resume,
        ):
            template_path: str = ""
            json_model = cv_model.model_dump_json()
            carbone_data = dict(data=json.loads(json_model), convertTo="pdf")
            try:
                ui.notify(f"Asking Carbone to create a PDF of our CV...", position="center")

                csdk = carbone_sdk.CarboneSDK(settings.carbone_access_token)
                template_path = "appdata/templates/simple_cv.docx"

                report_bytes, unique_report_name = await run.io_bound(
                    csdk.render,
                    template_path,
                    carbone_data
                )
                # Create the CV pdf
                with tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", suffix=".pdf",
                                                 delete=False) as temp_file:
                    with open(temp_file.name, mode='wb+') as fd:
                        fd.write(report_bytes)
                        fd.close()
                    if app.native.main_window:
                        os.system(f"open /tmp/{temp_file.name}")
                    else:
                        ui.download(temp_file.name, f"{app_model.settings.nomenclature}.pdf")
            except Exception as err:
                logger.error(err)
                logger.error(f"Can't create carbone output for /tmp/{app_model.settings.nomenclature}.pdf")

        def export_cv(
                app_model: AppModel,
                cv_model: resume_cv.Resume
        ):
            with tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", suffix=".json", delete=False) as temp_file:
                with open(temp_file.name, mode='w+', encoding="utf-8") as f:
                    # Make sure Windows BOM written to support utf-8 automatically
                    f.write('\ufeff')
                    json_data = cv_model.model_dump_json(indent=2)
                    f.write(json_data)
                    f.close()
                    ui.download(temp_file.name, f"{app_model.settings.nomenclature}.json")


        async def load_cv(app_model: AppModel, supabase: SupabaseClient):
            await self.open_json_cv(app_model, supabase)
            self.editor_content.refresh(app_model)

        with ui.row().classes("justify-center w-full"):
            ui.button('Import', icon="system_update_alt", on_click=lambda: load_cv(app_model, supabase))
            ui.button("Save changes", icon="save", on_click=lambda: self.save_model(app_model, cv, supabase))
            ui.button("Export JSON", icon="upgrade", on_click=lambda: export_cv(app_model, cv))
            ui.button("Create PDF", icon="picture_as_pdf", on_click=lambda: export_pdf(app_model, cv))

        with ui.tabs().props().classes('w-full') as layout_tabs:
            ui.tab('Form View')
            ui.tab('Data View')

        with ui.tab_panels(layout_tabs, value=app_model.settings.last_editor, on_change=lambda e: editor_changed(e)).props().classes('w-full') as layout_panels:
            with ui.tab_panel('Form View') as structured_view_panel:
                with ui.splitter(value=app_model.settings.last_splitter, on_change=splitter_changed).classes('w-full h-full') as splitter:
                    with splitter.before:
                        with ui.tabs().props(
                            'vertical active-color="primary" indicator-color="purple" align="justify"'
                        ).classes(
                            'w-full text-primary'
                        ) as tabs:
                            for section in self.editor_sections.values():
                                ui.tab(section['title'], icon=section['icon'])

                    with splitter.after:
                        with ui.tab_panels(tabs, value=app_model.settings.last_tab, on_change=lambda e: tab_changed(e)).classes(
                            'w-full'
                        ).props(
                            ''
                        ) as tab_panels:
                            for section in self.editor_sections.values():
                                with ui.tab_panel(section['title']) as tab_panel:
                                    self.tab_content(section, tabs, app_model, cv, cv_schema, supabase)
            with ui.tab_panel('Data View') as data_panel:
                self.json_editor_content(app_model, supabase)
