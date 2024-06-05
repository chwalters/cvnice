from nicegui import ui, app

from model.application import AppModel



async def help_content(app_model: AppModel):
    app.add_static_files('/images', 'images')
    ui.markdown(open("appdata/resources/help.md").read())


