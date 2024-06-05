from typing import Optional

from fastapi import Request
from fastapi.responses import RedirectResponse
from nicegui import ui

from model.application import AppModel, get_app_model
from services.analytics import PosthogAnalytics
from view.about import about_content
from view.composer import Composer
from view.editor import Editor
from view.help import help_content
from view.login import login_content, forgot_content, reset_password_content
from view.pagewrapper import page_wrapper
from view.privacy import privacy_content
from view.settings import settings_content
from view.splash import splash_content
from view.templates import TemplateView


def base_ui(app, settings, analytics: Optional[PosthogAnalytics] = None):

    async def page_layout(app_model: AppModel):
        await page_wrapper(
            app_model,
            settings,
            get_app_title(app_model),
            get_app_version(app_model),
            get_app_license(app_model)
        )

    def get_model() -> Optional[AppModel]:
        app_model: Optional[AppModel] = None
        username: Optional[str] = app.storage.user.get("username")
        if username is not None:
            app_model = get_app_model(username)
        return app_model

    def get_app_title(app_model: Optional[AppModel]) -> str:
        if app_model is None:
            return "CVNice"
        else:
            return f"{app_model.settings.nomenclature}Nice"

    def get_app_version(app_model: Optional[AppModel]) -> str:
        if app_model is None:
            return ""
        else:
            return app_model.settings.app_version

    def get_app_license(app_model: Optional[AppModel]) -> str:
        if app_model is None:
            return ""
        else:
            return app_model.settings.license_info

    @ui.page('/')
    async def index(request: Request):
        app_model: Optional[AppModel] = get_model()
        await page_layout(app_model)
        await splash_content(app_model)
        ui.separator()
        await login_content(app_model)
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/'})

    @ui.page('/me')
    async def edit_my_info(request: Request):
        editor: Editor = Editor()
        app_model: Optional[AppModel] = get_model()
        try:
            if app_model is not None:
                app_model.settings.last_tab = app.storage.user['editor_last_tab']
                app_model.settings.last_splitter = app.storage.user['editor_last_splitter']
        except KeyError:
            pass
        await page_layout(app_model)
        await editor.editor_content(app_model)
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/me'})

    @ui.page('/composer')
    async def get_a_job(request: Request):
        composer: Composer = Composer()
        app_model: Optional[AppModel] = get_model()
        await page_layout(app_model)
        await composer.composer_content(app_model)
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/composer'})

    @ui.page('/templates')
    async def job_templates(request: Request):
        templates: TemplateView = TemplateView()
        app_model: Optional[AppModel] = get_model()
        await page_layout(app_model)
        await templates.template_content(app_model)
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/templates'})


    @ui.page('/settings')
    async def settings_page(request: Request):
        app_model: Optional[AppModel] = get_model()
        await page_layout(app_model)
        await settings_content(app_model)
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/settings'})


    @ui.page('/help')
    async def help_page(request: Request):
        app_model: Optional[AppModel] = get_model()
        await page_layout(app_model)
        await help_content(app_model)
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/help'})


    @ui.page('/about')
    async def about_us(request: Request):
        app_model: Optional[AppModel] = get_model()
        await page_layout(app_model)
        await about_content(app_model)
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/about'})


    @ui.page('/privacy')
    async def about_us(request: Request):
        app_model: Optional[AppModel] = get_model()
        await page_layout(app_model)
        await privacy_content(app_model)
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/privacy'})


    @ui.page('/forgot')
    async def forgot(request: Request) -> Optional[RedirectResponse]:
        app_model: Optional[AppModel] = get_model()
        await page_layout(app_model)
        await forgot_content(request, app_model, position_class="absolute-center")
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/forgot'})


    @ui.page('/reset_password')
    async def reset_password(request: Request) -> Optional[RedirectResponse]:
        app_model: Optional[AppModel] = get_model()
        await page_layout(app_model)
        await reset_password_content(request, app_model, position_class="absolute-center")
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/reset_password'})


    @ui.page('/login')
    async def login() -> Optional[RedirectResponse]:
        app_model: Optional[AppModel] = get_model()
        await page_layout(app_model)
        await login_content(app_model, position_class="absolute-center")
        if analytics is not None:
            username: str = app.storage.user.get("username", "anonymous")
            analytics.capture(username, '$pageview', {'$current_url': 'https://app.cvnice.com/login'})
