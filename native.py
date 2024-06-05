from nicegui import app, ui
from nicegui.storage import RequestTrackingMiddleware
from starlette.middleware.sessions import SessionMiddleware

from utils.middleware.auth import AuthMiddleware
from view.index import base_ui

app.native.window_args['resizable'] = True
app.native.start_args['debug'] = True

from config import settings

base_ui(app, settings)

app.add_middleware(AuthMiddleware)
app.add_middleware(RequestTrackingMiddleware)
app.add_middleware(SessionMiddleware, secret_key=settings.nicegui_storage_secret)

ui.run(
    title="CVNice",
    native=True,
    window_size=(768, 1024),
    fullscreen=False,
    storage_secret=settings.nicegui_storage_secret
)