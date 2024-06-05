from nicegui import ui

from model.application import AppModel


async def about_content(app_model: AppModel):
    ui.image(source="images/logo.png").style("height: auto; max-width: 250px;").props("fit=contain").classes(
        "self-center")
    ui.markdown(open("appdata/resources/about.md").read())
