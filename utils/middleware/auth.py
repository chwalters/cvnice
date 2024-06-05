from typing import Optional

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from nicegui import ui, app, Client, storage
from fastapi.responses import RedirectResponse
from gotrue.errors import AuthApiError, AuthSessionMissingError
from gotrue import AuthResponse, Session
from supabase import Client as SupabaseClient
from loguru import logger

from model.application import AppModel, get_app_model, get_user_storage_bucket
from services.database.supa import get_client

unrestricted_page_routes = {'/', '/login', '/about', '/forgot', '/reset_password', '/help', '/privacy'}

class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.

    It redirects the user to the login page if they are not authenticated.
    """

    async def dispatch(self, request: Request, call_next):
        supabase: Optional[SupabaseClient] = None
        username: Optional[str] = app.storage.user.get('username', None)
        # logger.debug(f'Dispatch to url path: {request.url.path} with username: {username}')
        if username is not None:
            supabase = get_client(username)
        if supabase is not None:
            try:
                session: Session = supabase.auth.get_session()
            except AuthSessionMissingError:
                try:
                    supabase.auth.sign_out()
                    return RedirectResponse('/login')
                except AuthApiError as e:
                    return RedirectResponse('/login')
            try:
                access_token: str = app.storage.user.get('access_token', None)
                if access_token is None:
                    access_token = request.query_params.get('access_token', None)
                    refresh_token = request.query_params.get('refresh_token', None)
                    if access_token is not None:
                        if session is None:
                            if refresh_token is not None:
                                session = supabase.auth.refresh_session(refresh_token)
                if access_token is None:
                    if request.url.path in Client.page_routes.values() and request.url.path not in unrestricted_page_routes:
                        app.storage.user['referrer_path'] = request.url.path  # remember where the user wanted to go
                        return RedirectResponse('/login')
                else:
                    try:
                        refresh_token = request.query_params.get('refresh_token', app.storage.user.get('refresh_token', None))
                        if session is None:
                            session = supabase.auth.refresh_session(refresh_token)
                        user_info = session
                        if user_info is not None:
                            app.storage.user.update(
                                {
                                    'user_id': user_info.user.id,
                                    'access_token': access_token,
                                    'username': user_info.user.email
                                }
                            )
                            app_model: AppModel = get_app_model(user_info.user.email)
                            if app_model is not None:
                                app_model.bucket = get_user_storage_bucket(supabase, user_info.user.email)

                            referrer_path = app.storage.user.get('referrer_path', None)
                            if referrer_path is not None:
                                app.storage.user.update({'referrer_path': None})
                                return RedirectResponse(referrer_path)
                            else:
                                return await call_next(request)
                        else:
                            app.storage.user.clear()
                            return RedirectResponse('/login')

                    except AuthApiError as auth_api_error:
                        session: Session = supabase.auth.get_session()
                        if session is None:
                            app.storage.user.clear()
                        else:
                            try:
                                res: AuthResponse = supabase.auth.refresh_session(session.refresh_token)
                                if res is not None:
                                    user_info = supabase.auth.get_user(res.session.access_token)
                                    if user_info is not None:
                                        app.storage.user.update(
                                            {
                                                'username': app.storage.user.get('username'),
                                                'access_token': res.session.access_token,
                                                'profile': res.user.model_dump_json()
                                            }
                                        )
                                        try:
                                            ui.navigate.to(
                                                app.storage.user.get('referrer_path', '/composer'))  # go back to where the user wanted to go
                                        except RuntimeError as re:
                                            pass

                            except AuthSessionMissingError as auth_session_missing_error:
                                app.storage.user.clear()

                        return RedirectResponse('/login')
                    except Exception as e:
                        print(str(e))
                        return RedirectResponse('/login')

                return await call_next(request)
            except Exception as e:
                print(str(e))
                return RedirectResponse('/login')
        else:
            if request.url.path in Client.page_routes.values() and request.url.path not in unrestricted_page_routes:
                app.storage.user['referrer_path'] = request.url.path  # remember where the user wanted to go
                return RedirectResponse('/login')
            else:
                # logger.debug(f'Dispatch to url path: {request.url.path}')
                return await call_next(request)
