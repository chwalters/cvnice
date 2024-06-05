from nicegui import ui

from model.application import AppModel


async def settings_content(app_model: AppModel):
    ui.label("Settings").classes("text-h4")

    def toggle_dark_mode(e):
        dark = ui.dark_mode()
        if e.value:
            dark.enable()
        else:
            dark.disable()

    with ui.card() as settings_card:
        ui.input("Nomenclature").bind_value(app_model.settings, "nomenclature")
        ui.switch("Dark Mode", on_change=toggle_dark_mode).bind_value(app_model.settings, "dark_mode")

