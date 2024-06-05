import tempfile
from datetime import datetime
from pathlib import Path

from nicegui import ui, app, events
from storage3.utils import StorageException

from model.application import AppModel, get_user_storage_bucket
from services.database.supa import get_client
from supabase import Client as SupabaseClient
from loguru import logger

class TemplateView:

    def get_storage_exception_message(self, e: StorageException) -> str:
        error_msg: str = "Unknown error"
        if e is not None and e.args is not None and len(e.args) > 0:
            error_msg = e.args[0].get("message", "Unknown error")
        return error_msg


    def delete_template(self, username: str, supabase: SupabaseClient, filepath: str):
        try:
            supabase.storage.from_(username).remove(filepath)
        except StorageException as e:
            logger.error(e)
            ui.notify(
                self.get_storage_exception_message(e),
                color="negative"
            )
        finally:
            self.template_content.refresh()

    async def import_template(self, username, supabase: SupabaseClient):
        with ui.dialog() as open_dialog:
            async def load_template_from_user(e: events.UploadEventArguments):
                try:
                    supabase.storage.from_(username).upload(
                        file=e.content.read(), path=e.name,
                        file_options={
                            "content-type":
                            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"}
                    )

                except StorageException as se:
                    with ui.dialog() as error_dialog:
                        with ui.card().classes('w-full'):
                            ui.label("Upload Errors").classes("text-negative")
                            ui.textarea(value=str(self.get_storage_exception_message(se))).classes('w-full')
                            with ui.card_actions().classes('w-full justify-end'):
                                ui.button('Close', on_click=error_dialog.close)
                    result = await error_dialog
                finally:
                    open_dialog.close()

            ui.upload(
                on_upload=load_template_from_user
            ).classes(
                'w-full'
            ).props("accept='.docx,.xlsx,.pptx,.odt,.ods,.odg,.odp,.xhtml,.idml,.html,.xml'")

            result = await open_dialog

    def download_template(self, username: str, supabase: SupabaseClient, filepath: str):
        stem_prefix = Path(filepath).stem
        stem_suffix = Path(filepath).suffix
        with tempfile.NamedTemporaryFile(prefix=stem_prefix, suffix=stem_suffix, delete=False) as tmp_fp:
            named_temp_file = tmp_fp.file.name
            res = supabase.storage.from_(username).download(filepath)
            fd = open(named_temp_file, "wb")
            fd.write(res)
            fd.close()
            output_path = Path(named_temp_file)
            ui.download(output_path, filename=filepath)

    async def upload_template(self, username: str, supabase: SupabaseClient):
        await self.import_template(username, supabase)
        self.template_content.refresh()

    @ui.refreshable
    async def template_content(self, app_model: AppModel):
        form_controls = dict(
            templates=[],
        )

        with ui.column().classes("items-center w-full"):
            ui.label("Available Templates")
            ui.button('Import', icon="system_update_alt", on_click=lambda: self.upload_template(username, supabase))

        username = app.storage.user.get("username")
        supabase = get_client(username)

        if app_model.bucket is None:
            app_model.bucket = get_user_storage_bucket(supabase, username)

        if app_model.bucket is not None:
            form_controls.update(templates=supabase.storage.from_(username).list())
            print(form_controls.get("templates", []))

        with ui.row().classes("w-full") as row:
            for file in form_controls.get("templates", []):
                with ui.card().classes("col col-3") as file_card:
                    with ui.card_section().classes("justify-center w-full") as card_section:
                        with ui.row().classes("justify-center w-full") as info_row:
                            ui.icon(name="description").props("size=xl")
                            with ui.column().classes("justify-center items-center w-full") as info_column:
                                ui.label(file.get("name", "???.???"))
                                creation_date_str = file.get("created_at", "")
                                create_date = datetime.fromisoformat(creation_date_str)
                                ui.label(create_date.strftime('%Y/%m/%d'))
                    with ui.card_actions().classes("justify-center w-full") as card_actions:
                        with ui.row().classes("items-center justify-center w-full") as action_row:
                            ui.button(
                                "Download",
                                icon="download",
                                color="positive",
                                on_click=lambda: self.download_template(username, supabase, file.get("name"))
                            ).props("size=sm")
                            # ui.button("Rename", icon="drive_file_rename_outline", color="positive").props("size=sm")
                            ui.button(
                                "Delete",
                                icon="delete",
                                color="negative",
                                on_click=lambda e: self.delete_template(username, supabase, file.get("name")),
                            ).props("size=sm")

        # with ui.html().style("overflow: auto; min-width: 100%; max-width: 100%;") as content:
        #     content.set_content(  # height: 80vh;
        #         f'<embed title="simple_cv.docx" src="{path}" type="application/vnd.openxmlformats-officedocument.wordprocessingml.document" style="border: 1px solid gray; object-position: top center; height: 80vh; width: 100%;">')

