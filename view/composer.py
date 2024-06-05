import json
import os
import re
from json import JSONDecodeError
from pathlib import Path
from typing import Optional, List

from email_validator import validate_email, EmailNotValidError
from glom import assign, glom, PathAccessError
from loguru import logger
import carbone_sdk
from nicegui import ui, run, app
from pydantic import HttpUrl, EmailStr, AnyUrl, TypeAdapter
from supabase import Client as SupabaseClient

from config import settings
from model import resume_cv
from model.application import AppModel
from model.jobs import JobOpening, HiringManager, JobType, WorkMode
from model.prompts import Prompter, get_job_prompts, DEFAULT_IT_PROMPTS
from model.resume_cv import Resume
from services.basic_lingua.blingua_sdk_python.src.blinguasdk import BlinguaSDK
from services.basic_lingua.blingua_sdk_python.src.blinguasdk.models import errors
from services.database.db_job import JobDB
from services.database.supa import get_client
from view.render import TemplateRenderer




class Composer:
    my_jobs: Optional[List[JobOpening]] = []
    selected_job_opening: Optional[JobOpening]  = None
    job_db: Optional[JobDB] = None
    selection_index: int = 0

    composer_sections = dict(
        basics=dict(
            title="Leads",
            prop="basics",
            icon="person",
            tab_index=0,
        ),
        work=dict(
            title="Applied for",
            prop="work",
            icon="work",
            tab_index=1,
        ),
        volunteer=dict(
            title="Interviews",
            prop="volunteer",
            icon="volunteer_activism",
            tab_index=2,
        ),
    )

    def validate_emailinput(self, v):
        retVal = None
        if v is not None and len(v) > 0:
            try:
                validate_email(v)
                retVal = None
            except EmailNotValidError as e:
                retVal = "Invalid email"
        return retVal

    def fetch_cv(self, app, app_model: AppModel) -> Resume:
        my_cv: Resume = app_model.personae[0].cv_resume
        try:
            name: str = glom(my_cv, 'basics.name')
        except PathAccessError as e:
            my_cv = None

        if my_cv is None:
            logger.debug(f"No resume available, fetching from back end")
            user_id = app.storage.user.get("user_id", None)
            if user_id is not None:
                username = app.storage.user.get("username", None)
                if username is not None:
                    supabase: SupabaseClient = get_client(username)
                    if supabase is not None:
                        my_auth = supabase.auth.get_session().user.id
                        print(f'Trying to fetch personae for user: {user_id}, auth_id ={my_auth}')
                        response = supabase.table('personae').select('cv_resume').eq('owner', user_id).execute()
                        if response is not None:
                            if len(response.data) > 0:
                                my_cv = TypeAdapter(resume_cv.Resume).validate_json(
                                    response.data[0]['cv_resume'])
                                app_model.personae[0].cv_resume = my_cv
                            else:
                                print('Zero personae loaded')
                                app.storage.user.clear()
                        else:
                            print('No personae found')
                            app.storage.user.clear()
                    else:
                        print('No user_id to fetch personae for user')
                        app.storage.user.clear()
        else:
            logger.debug(f"Our cv is available, fetching from back end")

        return my_cv

    @ui.refreshable
    async def composer_content(self, app_model: AppModel):
        form_controls = dict(
            spinner_visible=False,
            job_offer_input="",
            valid_inputs=False,
            apply_spinner_visible=False,
            enable_downloads=False,
            cv_path=None,
            cover_path=None,
            cv_template=None,
            cover_template=None,
            cv_format="docx",
            cover_format="docx",
            job_opening_tabel=None,
            model_dicts=[],
        )
        self.selected_job_opening = None
        user_id = app.storage.user.get("user_id", None)

        if user_id is not None:
            username = app.storage.user.get("username", None)
            if username is not None:
                supabase: SupabaseClient = get_client(username)
                if supabase is not None:
                    if self.job_db is None:
                        self.job_db = JobDB(supabase)
                    my_auth = supabase.auth.get_session().user.id
                    logger.info(f'Trying to fetch jobs for user: {user_id}, auth_id ={my_auth}')
                    self.my_jobs = self.job_db.fetch_jobs(user_id)
                    if self.my_jobs is not None:
                        if len(self.my_jobs) > 0:
                            self.selected_job_opening = self.my_jobs[0]
                        else:
                            logger.warning('Zero jobs loaded')
                    else:
                        self.my_jobs = []
                        logger.warning('No job openings found')

        else:
            logger.warning('No user_id to fetch job_openings for user')



        def create_lead(app_model: AppModel):
            pass
        def tab_changed(e):
            logger.debug(f"Composer tab changed: {e.value}")
            # app_model.settings.last_tab = e.value
            # app.storage.user['editor_last_tab'] = app_model.settings.last_tab

        def splitter_changed(e):
            logger.debug(f"Composer splitter changed: {e.value}")
            # app_model.settings.last_csplitter = e.value
            # app.storage.user['editor_last_splitter'] = app_model.settings.last_splitter


        @ui.refreshable
        def tab_content(section, tabs):

            columns = [
                {
                    "name": "created_ad",
                    "label": "Date",
                    "field": "created_at",
                    "required": False,
                    "sortable": True,
                    ":format": 'value => value = Quasar.date.formatDate(value, "YYYY/MM/DD")',
                },
                {
                    "name": "title",
                    "label": "Title",
                    "field": "title",
                    "required": False,
                    "sortable": True,
                    "align": "left",
                },
                {
                    "name": "company",
                    "label": "Company",
                    "field": "company",
                    "required": False,
                    "sortable": True,
                    "align": "left",
                },
                {
                    "name": "location",
                    "label": "Location",
                    "field": "location",
                    "required": False,
                    "sortable": True,
                    "align": "left",
                },
                {
                    "name": "description",
                    "label": "Summary",
                    "field": "description",
                    "required": False,
                    "sortable": True,
                    "align": "left",
                    ":format": "value => (value.length > 55) ? value.substring(0, 54) + '...' : value"
                },
            ]

            with (ui.card().classes('w-full').style('overflow: auto;') as blingua_test_card):
                def select_job(e):
                    self.selected_job_opening = None
                    form_controls.update(cv_path=None)
                    form_controls.update(cover_path=None)

                    for job in self.my_jobs:
                        if e is not None and e.selection is not None and len(e.selection) > 0:
                            if job.id == e.selection[0].get("id", None):
                                self.selected_job_opening = job
                                jtable = form_controls["job_opening_table"]
                                jtable.selected = [jtable.rows[self.my_jobs.index(job)]]
                                break
                        else:
                            self.selected_job_opening = None
                            break
                    selected_job_content.refresh()

                @ui.refreshable
                def job_opening_table_content():
                    form_controls.update(model_dicts=[json.loads(d.model_dump_json()) for d in self.my_jobs])

                    with ui.table(
                        rows=form_controls.get("model_dicts", []),
                        columns=columns,
                        selection="single",
                        on_select=lambda e: select_job(e),
                        row_key="id"
                    ).props(
                        "dense flat"
                    ).classes("w-full") as job_opening_table:
                        form_controls.update(job_opening_table=job_opening_table)
                        if self.selected_job_opening is not None:
                            job_opening_table.selected = [job_opening_table.rows[self.my_jobs.index(self.selected_job_opening)]]

                job_opening_table_content()

                with ui.row().classes("w-full"):
                    ui.icon("add")
                    ui.label("Paste New Job Offer Below")

                def job_offer_input_changed(e):
                    if e and e.value and len(e.value) > 0:
                        form_controls.update(valid_inputs=True)
                    else:
                        form_controls.update(valid_inputs=False)

                with ui.textarea(
                        'Job Offer',
                        value=form_controls['job_offer_input'],
                        on_change=lambda e: job_offer_input_changed(e)
                ).classes(
                    'w-full'
                ).bind_value(form_controls, "job_offer_input") as input_text_area:
                    pass
                async def run_lingua_test(spinner):


                    have_input: bool = input_text_area.value is not None and len(input_text_area.value) > 0
                    if not have_input:
                        ui.notify(f"Please paste a job offer first...")
                        return
                    else:
                        job_opening = self.job_db.create_job(
                            user_id,
                            JobOpening(
                                id=-1,
                                title="*Paste into job offer above for AI recognition*",
                                company="",
                                description="""
                                                                    """,
                                location="",
                                url="http://blah",
                                hiring_manager=HiringManager(
                                    name="",
                                    email=None,
                                    phone=""
                                ),
                                job_type=JobType.FULL_TIME,
                                work_mode=WorkMode.REMOTE,
                                keywords="",
                                owner=None
                            )
                        )
                        self.my_jobs.insert(0, job_opening)

                    form_controls['spinner_visible'] = True
                    spinner.update()

                    notif = ui.notification(
                        'Analyzing job offer',
                        position="top",
                        spinner=True,
                        type="ongoing",
                        multi_line=False
                    )

                    prompter: Prompter = Prompter(settings.gemini_api_key)
                    prompts: Optional[dict] = get_job_prompts(
                        "Information Technology (IT)",
                        DEFAULT_IT_PROMPTS
                    )
                    for key, value in prompts.items():
                        question = value.get("question", None)
                        target_path = value.get("result_path", None)
                        if question is not None and target_path is not None:
                            notif.message = f"Asking the AI: {question}"
                            res = await run.io_bound(prompter.qna, question, input_text_area.value.encode("utf-8"))
                            if res is not None:
                                if "email" in target_path:
                                    try:
                                        validation_error = self.validate_emailinput(res)
                                        if validation_error is None:
                                            assign(job_opening, target_path, res)
                                    except:
                                        assign(job_opening, target_path, None)
                                        pass
                                elif "url" in target_path:
                                    try:
                                        valid_url = AnyUrl(res)
                                        assign(job_opening, target_path, valid_url)
                                    except:
                                        assign(job_opening, target_path, None)
                                        pass
                                else:
                                    if not "no " in res.lower() and not "does not" in res.lower() and not "is not" in res.lower():
                                        assign(job_opening, target_path, res)
                                    else:
                                        assign(job_opening, target_path, "")

                    # process keywords
                    try:
                        if job_opening.keywords is not None:
                            res_list = job_opening.keywords.split(",")
                            if len(res_list) < 2:
                                res_list = job_opening.keywords.split("*")
                            if len(res_list) < 2:
                                res_list = job_opening.keywords.split("-")
                            if len(res_list) > 2:
                                res_list = [re.sub(r'[^A-Za-z0-9 ]+', '', s.strip()) for s in res_list if s is not None and len(s) > 0]
                                job_opening.keywords = str([s for s in res_list if s not in job_opening.keywords.split(',')])
                                keywords_as_str: str = ", ".join(job_opening.keywords.split(','))
                                job_opening.keywords = re.sub(r'[^A-Za-z0-9, ]+', '', keywords_as_str)
                                if len(job_opening.keywords) < 1:
                                    job_opening.keywords = None
                            else:
                                job_opening.keywords = None
                    except:
                        pass

                    notif.message = f"Asking the AI to summarize the job offer"
                    res = await run.io_bound(
                        prompter.summarize,
                        input_text_area.value.encode("utf-8"),
                        summary_length="short"
                    )
                    if res is not None:
                        job_opening.description = res
                    else:
                        job_opening.description = ""

                    form_controls['spinner_visible'] = False
                    form_controls.update(cv_path=None)
                    form_controls.update(cover_path=None)
                    spinner.update()
                    self.job_db.update(job_opening)
                    self.selected_job_opening = job_opening
                    selected_job_content.refresh()
                    job_opening_table_content.refresh()

                    notif.dismiss()

                with ui.card_actions().classes("row full-width") as actions:
                    with ui.row().classes("row full-width justify-center"):
                        ai_spinner = ui.spinner('puff', size="lg").bind_visibility_from(form_controls, "spinner_visible")
                        ui.button(
                            'Run AI Analysis...',
                            on_click=lambda: run_lingua_test(ai_spinner)
                        ).bind_enabled_from(
                            form_controls,
                            "valid_inputs"
                        )

            ui.label(section['title'])

            @ui.refreshable
            def selected_job_content():
                if self.selected_job_opening is not None:
                    for job_opening in [self.selected_job_opening]:
                        with ui.card().classes("w-full") as job_card:
                            with ui.card_section().classes("w-full") as job_section:
                                with ui.row().classes("row items-center text-center w-full text-primary") as title_row:
                                    ui.badge(f"{job_opening.created_at.strftime('%Y/%m/%d')}")

                                    ui.label(
                                        job_opening.title
                                    ).classes(
                                        "w-full text-primary text-h4"
                                    ).bind_text(
                                        job_opening, "title"
                                    )

                                    ui.label(
                                        job_opening.company
                                    ).classes(
                                        "w-full text-primary text-h6"
                                    ).bind_text(
                                        job_opening, "company"
                                    )

                                ui.input(
                                    "Job Title",
                                    value=job_opening.title
                                ).classes(
                                    "w-full"
                                ).bind_value(job_opening, "title")

                                ui.input(
                                    "Company",
                                    value=job_opening.company
                                ).classes(
                                    "w-full"
                                ).bind_value(job_opening, "company")

                                ui.input(
                                    "Location",
                                    value=job_opening.location
                                ).classes(
                                    "w-full"
                                ).bind_value(job_opening, "location")

                                ui.markdown(
                                    job_opening.description
                                ).classes(
                                    "w-full"
                                ).bind_content(
                                    job_opening, "description"
                                )

                                ui.separator()

                                def validate_url(v):
                                    retVal = None
                                    if v is not None and len(v) > 0:
                                        try:
                                            url = HttpUrl(v)
                                            retVal = None
                                        except:
                                            retVal = "Invalid URL"
                                    return retVal

                                validation_lambda = validate_url
                                forward_lambda = lambda u: u
                                backward_lambda = lambda u: str(u) if u is not None else None
                                type_prop = 'type="url"'

                                with ui.input("url", validation=validation_lambda).bind_value(
                                        job_opening,
                                        "url",
                                        backward=backward_lambda,
                                        forward=forward_lambda
                                ).props(
                                    'bottom-slots ' + type_prop
                                ) as url_input:
                                    def open_url():
                                        logger.info(f"Navigating to {str(job_opening.url)}")
                                        ui.navigate.to(str(job_opening.url), new_tab=True)
                                    with url_input.add_slot('prepend'):
                                        ui.button(
                                            "",
                                            icon="link",
                                            on_click=open_url
                                        ).props("size=xs")


                                ui.separator()
                                ui.select(
                                    [i.value for i in JobType],
                                    value=job_opening.job_type,
                                    label="Job Type"
                                ).classes(
                                    "w-full"
                                ).bind_value(
                                    job_opening, "job_type"
                                )
                                ui.select(
                                    [i.value for i in WorkMode],
                                    value=job_opening.work_mode,
                                    label="Work Mode"
                                ).classes(
                                    "w-full"
                                ).bind_value(
                                    job_opening, "work_mode"
                                )

                                if job_opening.hiring_manager is not None:
                                    with ui.input(
                                        'Name',
                                        value=job_opening.hiring_manager.name
                                    ).bind_value(
                                        job_opening.hiring_manager, "name"
                                    ) as hiring_manager_name_input:
                                        with hiring_manager_name_input.add_slot("prepend") as prepend_slot:
                                            ui.icon("person", color="primary")
                                    with ui.input(
                                        'Email',
                                        value=job_opening.hiring_manager.email,
                                        validation=self.validate_emailinput
                                    ).props(
                                        'type=email'
                                    ).bind_value(
                                        job_opening.hiring_manager, "email"
                                    ) as email_input:
                                        with email_input.add_slot("prepend") as prepend_slot:
                                            ui.icon("email", color="primary")
                                    with ui.input(
                                            'Phone',
                                            value=job_opening.hiring_manager.phone
                                    ).bind_value(
                                        job_opening.hiring_manager, "phone"
                                    ) as phone_input:
                                        with phone_input.add_slot("prepend") as prepend_slot:
                                            ui.icon("phone", color="primary")
                            with ui.card_section().classes("w-full") as keywords_section:
                                with ui.row().classes("row items-center text-center w-full"):
                                    if job_opening.keywords is not None:
                                        for keyword in job_opening.keywords.split(','):
                                            ui.html(f'{keyword}', tag='q-chip').props("outline color='blue-10'")

                            with ui.card_section().classes("w-full") as application_section:
                                with ui.textarea().classes("w-full") as cover_letter_text_area:
                                    pass

                            def save_job():
                                have_input: bool = job_opening is not None
                                if not have_input:
                                    ui.notify('No selected job', color="negative")
                                else:
                                    try:
                                        self.job_db.update(job_opening)
                                        job_opening_table_content.refresh()
                                        ui.notify('Job saved...', color="positive")
                                    except:
                                        ui.notify('Error saving job', color="negative")


                            def delete_job():
                                have_input: bool = job_opening is not None
                                if not have_input:
                                    ui.notify('No selected job')
                                else:
                                    self.job_db.delete(job_opening)
                                    self.my_jobs.remove(job_opening)
                                    select_job(None)
                                    selected_job_content.refresh()
                                    job_opening_table_content.refresh()
                            async def apply(spinner):

                                have_input: bool = job_opening is not None
                                if not have_input:
                                    ui.notify(f"Please create a job offer first...")
                                    return

                                notif = ui.notification(
                                    'Applying for job offer',
                                    position="top",
                                    spinner=True,
                                    type="ongoing",
                                    multi_line=False
                                )

                                form_controls['apply_spinner_visible'] = True
                                spinner.update()

                                if self.job_db is not None:
                                    self.job_db.update(job_opening)

                                my_cv: Resume = self.fetch_cv(app, app_model)
                                custom_cv: Resume = my_cv.model_copy(deep=True)
                                if custom_cv.skills is not None:
                                    custom_cv.skills.clear()
                                relevant_skills = []
                                if my_cv.skills is not None:
                                    for skill in my_cv.skills:
                                        if job_opening.keywords is not None:
                                            for keyword in job_opening.keywords.split(','):
                                                if keyword in skill.keywords or keyword in skill.summary:
                                                    if skill not in relevant_skills:
                                                        relevant_skills.append(skill)
                                if custom_cv.skills is not None:
                                    custom_cv.skills.extend(relevant_skills)
                                json_model = custom_cv.model_dump_json()
                                if json_model is not None:
                                    logger.debug(json_model)
                                    notif.message = f"Asking the AI to generate a cover letter"

                                    s = BlinguaSDK()
                                    prompt = f"""
                                    Given the following job offer, write a cover letter for my job application:
                                    {job_opening.description}
                                    
                                    """
                                    try:
                                        res = await run.io_bound(
                                            s.text_generate_wrapper_text_generate_length_post,
                                            length="medium",
                                            request_body=prompt.encode("utf-8"),
                                            api_key=settings.gemini_api_key
                                        )
                                        if res.text_result is not None:
                                            cover_letter_raw = res.text_result.results
                                            if cover_letter_raw is not None and len(cover_letter_raw) > 0:
                                                replacements={
                                                    "[Your Name]": "",
                                                    "[Your Address]": "",
                                                    "[City, Postal Code]": "",
                                                    "[Email Address]": "",
                                                    "[Phone Number]": "",
                                                    "[Date]": "",
                                                    "[Contact Name( if available)]": "",
                                                    "[Address( if available)]": "",
                                                    "[Address]": "",
                                                    "[City, Postal Code( if available)]": ""
                                                }
                                                for (k, v) in replacements.items():
                                                    cover_letter_raw = cover_letter_raw.replace(k,v)

                                            cover_letter_text_area.value = cover_letter_raw
                                            template_renderer: TemplateRenderer = TemplateRenderer(app_model)

                                            try:
                                                ui.notify(f"Asking Carbone to create a {form_controls.get('cv_format')} of our CV...")

                                                rendered_file_path = await run.io_bound(
                                                    template_renderer.render,
                                                    json.loads(json_model),
                                                    form_controls.get("cv_template", None),
                                                    username,
                                                    supabase,
                                                    format=form_controls.get("cv_format", "docx"),
                                                )
                                                if rendered_file_path is not None:
                                                    if app.native.main_window:
                                                        os.system(f"open {rendered_file_path}")
                                                    else:
                                                        form_controls['cv_path'] = app.add_media_file(local_file=rendered_file_path, single_use=False)

                                            except Exception as err:
                                                logger.error(err)
                                                logger.error(f"Can't create carbone output rendered CV")

                                            fixed_text = cover_letter_text_area.value # "\r\n".join([s for s in cover_letter_text_area.value.splitlines() if s])
                                            cover_letter_model = dict(cv=json.loads(json_model), coverletter=fixed_text)
                                            try:
                                                notif.message = f"Asking Carbone to create a draft cover letter"

                                                rendered_coverletter_path = await run.io_bound(
                                                    template_renderer.render,
                                                    cover_letter_model,
                                                    None,
                                                    username,
                                                    supabase,
                                                    document_type="cover",
                                                    format=form_controls.get("cover_format", "docx"),
                                                )
                                                if app.native.main_window:
                                                    os.system(f"open {rendered_coverletter_path}")
                                                else:
                                                    form_controls['cover_path'] = app.add_media_file(local_file=rendered_coverletter_path, single_use=False)
                                            except Exception as err:
                                                logger.error(err)
                                                logger.error("Can't create carbone output rendered cover letter")

                                        else:
                                            cover_letter_text_area.value = ""
                                    except Exception as err:
                                        ui.notify(f"AI failed for some reason. Trying again might work", color="negative")

                                form_controls['apply_spinner_visible'] = False
                                spinner.update()
                                notif.dismiss()
                                action_content.refresh()

                            @ui.refreshable
                            def action_content():
                                templates: Optional[List[str]] = supabase.storage.from_(username).list()
                                with ui.card_actions().classes("q-pa-md row full-width") as actions:
                                    with ui.row().classes("q-pa-md row full-width justify-center"):
                                        apply_spinner = ui.spinner('puff', size="lg").bind_visibility_from(
                                            form_controls,
                                            "apply_spinner_visible"
                                        )
                                        if len(templates) > 0:
                                            with ui.select(
                                                [f.get('name') for f in templates],
                                                label="CV Template",
                                                value=glom(templates[0], "name")
                                            ).props('bottom-slots stack-label clearable').bind_value(
                                                form_controls, "cv_template"
                                            ).style('min-width: 250px;') as cv_template_selection:
                                                with cv_template_selection.add_slot("hint"):
                                                    ui.label("Choose CV Template")
                                            with ui.element("span").classes("q-gutter-sm"):
                                                ui.label("Output Format")
                                                with ui.radio(
                                                        ['pdf', 'docx'],
                                                        value=form_controls.get("cv_format")
                                                  ).bind_value(form_controls, "cv_format"):
                                                    pass

                                            with ui.select(
                                                    [f.get('name') for f in templates],
                                                    label="Cover Template",
                                                    value=glom(templates[0], "name")
                                            ).props('bottom-slots stack-label clearable').bind_value(
                                                form_controls, "cover_template"
                                            ).style('min-width: 250px;') as cover_template_selection:
                                                with cover_template_selection.add_slot("hint"):
                                                    ui.label("Choose Cover Letter Template")
                                            with ui.element("span").classes("q-gutter-sm"):
                                                ui.label("Output Format")
                                                with ui.radio(
                                                        ['pdf', 'docx'],
                                                        value=form_controls.get("cover_format")
                                                  ).bind_value(form_controls, "cover_format"):
                                                    pass

                                    with ui.row().classes("q-pa-md row full-width justify-center"):

                                        ui.button("Apply", on_click=lambda: apply(apply_spinner)).props('color=positive')
                                        ui.button('Save', icon="save", on_click=save_job).props('color=positive')
                                        ui.button("Delete", on_click=delete_job).props('color=negative')

                                        def type_suffix(path_key: str) -> Optional[str]:
                                            file_type: Optional[str] = None
                                            path: Optional[str] = form_controls.get(path_key, None)
                                            if path is not None:
                                                file_type = Path(path).suffix
                                            logger.debug(f"Determined {file_type} for {path_key} using {path}")
                                            return file_type

                                        def icon_name(path_key: str) -> Optional[str]:
                                            iname = "edit_document"
                                            suffix = type_suffix(path_key)
                                            if suffix is not None:
                                                if suffix == ".pdf":
                                                    iname = "picture_as_pdf"
                                                elif suffix == ".docx":
                                                    iname = "edit_document"
                                                else:
                                                    pass # will work on more perhaps
                                            logger.debug(f"Determined icon {iname} for {path_key} using {suffix}")
                                            return iname


                                        ui.button(
                                            f"{app_model.settings.nomenclature}",
                                            icon=icon_name("cv_path"),
                                            on_click=lambda: ui.download(form_controls['cv_path'], filename=f"cv{type_suffix('cv_path')}"),
                                        ).bind_visibility_from(form_controls, "cv_path")
                                        ui.button(
                                            f"Cover Letter",
                                            icon=icon_name('cover_path'),
                                            on_click=lambda: ui.download(form_controls['cover_path'], filename=f"cover{type_suffix('cover_path')}"),
                                        ).bind_visibility_from(form_controls, "cover_path")

                    action_content()
            selected_job_content()


        with ui.column().classes("items-center w-full q-pa-md"):
            ui.label("Job Opportunities/Leads")
            tab_content(self.composer_sections['basics'], None)
