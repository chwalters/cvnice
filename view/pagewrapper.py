from nicegui import ui, app

from config import Settings
from model.application import AppModel
from .menus import top_menu


async def page_wrapper(app_model: AppModel, settings: Settings, app_title: str, version: str, copyright: str) -> None:
    dark_mode = ui.dark_mode()
    if app_model is not None:
        if app_model.settings.dark_mode:
            dark_mode.enable()
        else:
            dark_mode.disable()

    ui.colors(
        primary='#0F588C', # '#5898d4',
        secondary='#26a69a',
        accent='#9c27b0',
        dark='#1d1d1d',
        positive='#21ba45',
        negative='#c10015',
        info='#31ccec',
        warning='#f2c037'
    )

    ui.add_head_html("""
<meta charset="utf-8">
""")
    ui.add_head_html("""
      <script>
         var url = window.location.href;
         newUrl = url.replace("#", "?");
         if (url !== newUrl) {
             window.location.replace(newUrl);
         }
      </script>
    """)

    with ui.header(
            elevated=True
    ).props(
        "reveal"
    ).classes(
        'items-center justify-content-center'
    ):
        top_menu("Welcome!", app_model)
        ui.label(app_title)
        ui.space()
        with ui.row().classes('pa-xs'):
            ui.label(f"{app.storage.user.get('username', '')}")
            if version is not None and len(version) > 0:
                ui.label(f"Version: {version}")

    with ui.footer(elevated=False).props("reveal").classes("row justify-center items-center content-start"):
        if settings.dev_mode:
            ui.label(f"// Development Mode Enabled")
        ui.label(f"// {copyright} //")
        ui.button("Splash Images from DeepAI",
                  on_click=lambda x: ui.navigate.to("https://deepai.org/machine-learning-model/text2img", new_tab=True)).props("color=positive size=sm")

