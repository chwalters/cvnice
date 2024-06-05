from nicegui import ui, app
from model.application import AppModel

def top_menu(username: str, app_model: AppModel) -> None:
    auth_item_name = 'Login'
    auth_icon_name = 'login'
    access_token = app.storage.user.get("access_token", None)
    if access_token is not None:
        auth_item_name = 'Logout'
        auth_icon_name = 'logout'

    with ui.button(icon='menu'):
        with ui.menu() as menu:
            with ui.menu_item():
                with ui.item_section().classes('self-center'):
                    ui.image("images/logo.png").style("height: auto; max-width: 80px;").props("fit=contain").classes('self-center')

            with ui.menu_item(on_click=lambda: ui.navigate.to("/")):
                with ui.item_section().props('avatar'):
                    ui.icon(name="home")
                with ui.item_section().props("item-label"):
                    ui.label(text="Home")
            ui.separator()
            with ui.menu_item(on_click=lambda x: ui.navigate.to("/me")):
                with ui.item_section().props('avatar'):
                    ui.icon(name="article")
                with ui.item_section().props("item-label"):
                    if app_model is not None:
                        ui.label(text=f"{app_model.settings.nomenclature}")
                    else:
                        ui.label(text="CV")
            ui.separator()
            with ui.menu_item(on_click=lambda: ui.navigate.to("/composer")):
                with ui.item_section().props('avatar'):
                    ui.icon(name="paid")
                with ui.item_section().props("item-label"):
                    ui.label(text="Jobs")
            ui.separator()
            with ui.menu_item(on_click=lambda x: ui.navigate.to("/templates")):
                with ui.item_section().props('avatar'):
                    ui.icon(name="edit_document")
                with ui.item_section().props("item-label"):
                    ui.label(text="Templates")
            ui.separator()
            with ui.menu_item(on_click=lambda: ui.navigate.to("/settings")):
                with ui.item_section().props('avatar'):
                    ui.icon(name="settings")
                with ui.item_section().props("item-label"):
                    ui.label(text="Settings")
            ui.separator()
            with ui.menu_item(on_click=lambda: ui.navigate.to("/help")):
                with ui.item_section().props('avatar'):
                    ui.icon(name="help")
                with ui.item_section().props("item-label"):
                    ui.label(text="Help")
            with ui.menu_item(on_click=lambda: ui.navigate.to("/about")):
                with ui.item_section().props('avatar'):
                    ui.icon(name="info")
                with ui.item_section().props("item-label"):
                    ui.label(text="About")
            with ui.menu_item(on_click=lambda: ui.navigate.to("/privacy")):
                with ui.item_section().props('avatar'):
                    ui.icon(name="policy")
                with ui.item_section().props("item-label"):
                    ui.label(text="Privacy")
            ui.separator()
            with ui.menu_item(on_click=lambda:(app.storage.user.clear(), ui.navigate.to('/login'))):
                with ui.item_section().props('avatar'):
                    ui.icon(name=auth_icon_name)
                with ui.item_section().props("item-label"):
                    ui.label(text=auth_item_name)

