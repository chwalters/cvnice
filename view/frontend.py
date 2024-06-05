from fastapi import FastAPI
from nicegui import ui, app
from nicegui.storage import RequestTrackingMiddleware
from starlette.middleware.sessions import SessionMiddleware
from services.analytics import PosthogAnalytics
from typing import Optional
from config import Settings
from utils.middleware.auth import AuthMiddleware
from view.index import base_ui

def init(fastapi_app: FastAPI, settings: Settings, analytics: Optional[PosthogAnalytics] = None) -> None:

    base_ui(app, settings, analytics)

    fastapi_app.add_middleware(AuthMiddleware)
    fastapi_app.add_middleware(RequestTrackingMiddleware)
    fastapi_app.add_middleware(SessionMiddleware, secret_key=settings.nicegui_storage_secret)

    ui.run_with(
        fastapi_app,
        title=f"CVNice",
        storage_secret=settings.nicegui_storage_secret,
    )





