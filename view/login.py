from typing import Optional

import jwt
from gotrue import AuthResponse, Session, Options, UserAttributes
from gotrue.errors import AuthApiError, AuthInvalidCredentialsError
from nicegui import ui, app
from pydantic import TypeAdapter
from starlette.requests import Request
from starlette.responses import RedirectResponse
from storage3.types import CreateOrUpdateBucketOptions

from model import resume_cv
from model.application import AppModel, get_app_model, get_user_storage_bucket
from model.resume_cv import Basics, Meta, Location
from services.database.supa import get_client
from supabase import Client as SupabaseClient
from loguru import logger
from config import settings

async def reset_password_content(request: Request, app_model: AppModel, position_class: str = 'absolute-center'):

    supabase: Optional[SupabaseClient] = None

    async def reset_password_flow() -> None:
        target_username = username.value
        target_password = password.value
        valid = None
        if (target_username is None) or (target_password is None):
            valid = "Please enter your new password"
        if (len(target_username) == 0) or (len(target_password) == 0):
            valid = "Please enter a new password"
        my_username = app.storage.user.get("username")
        if my_username is None:
            valid = "Username not matched"
        else:
            if my_username != target_username:
                valid = "Username not matched"
        if valid is not None:
            ui.notify(valid)
        else:
            supabase = get_client(my_username)
            try:
                supabase.auth.update_user({"id": username.value, "password": password.value})
                with ui.dialog() as confirmation_dialog, ui.card():
                    ui.label(f"Password changed")
                    with ui.row().classes('w-full justify-center'):
                        ui.button('Back to login...', color="positive", icon="login",
                                  on_click=lambda: confirmation_dialog.submit(True))

                result = await confirmation_dialog
                if result is True:
                    app.storage.user.clear()
                    supabase.auth.sign_out()
                    ui.navigate.to('/login')

            except Exception as e:
                ui.notify(str(e))

    try:
        access_token = request.query_params.get('access_token', None)
        if access_token is not None:
            contents = jwt.decode(access_token, settings.supabase_jwt_secret, audience="authenticated", algorithms=["HS256"])
            # contents = jwt.decode(access_token, options={'verify_signature': False})
            if contents is not None:
                token_username = contents.get('email', None)
                if token_username is not None:
                    app.storage.user["username"] = token_username
                    refresh_token = request.query_params.get('refresh_token', None)
                    if refresh_token is not None:
                        supabase = get_client(token_username)
                        if supabase is not None:
                            session = supabase.auth.refresh_session(refresh_token)
                            if session is not None:

                                ui.label('You can now change your password')
                                with ui.card().classes(f'{position_class} col col-6'):
                                    ui.image(f"images/logo.png")
                                    ui.label('Update your password').classes('self-center h2')
                                    username = ui.input(
                                        'Username',
                                        value=app.storage.user.get("username", "")
                                    ).on(
                                        'keydown.enter',
                                        reset_password_content
                                    ).classes(
                                        "row w-full"
                                    ).props("readonly")

                                    password = ui.input('New Password', password=True, password_toggle_button=True).on('keydown.enter', reset_password_flow).classes("row w-full")
                                    with ui.card_actions().classes("row justify-center w-full"):
                                        ui.button('Update password', on_click=reset_password_flow).on('keydown.enter', reset_password_flow)
    except:
        app.storage.user.clear()
        ui.navigate.to('/login')


async def forgot_content(request: Request, app_model: AppModel, position_class: str = 'self-center'):
    def start_reset_flow(email) -> None:
        if email is not None and len(email) > 0:
            try:
                supabase: SupabaseClient = get_client(email)
                res: AuthResponse = supabase.auth.reset_password_email(email, options=Options(
                    redirect_to="https://app.cvnice.com/reset_password"
                ))
                ui.notify('Check your email', color='positive')
            except Exception as e:
                ui.notify('Invalid username (email) provided', color='negative')
        else:
            ui.notify('You must provide an email address', color='negative')

    access_token = request.query_params.get('access_token', None)

    if access_token is None:
        print("No access token in forgot password")
        with ui.card().classes(f'{position_class} col col-6'):
            ui.image(f"images/logo.png")
            ui.label('Forgot password?').classes('self-center h2')
            username = ui.input('Username/Email').on('keydown.enter', lambda: start_reset_flow(username.value)).classes("row w-full")
            with ui.card_actions().classes("row justify-center w-full"):
                ui.button('Reset password', on_click=lambda: start_reset_flow(username.value))
            with ui.card_actions().classes("row justify-center w-full"):
                ui.label('Note! The app is completely free to use for now')
    return None
async def login_content(app_model: AppModel, position_class: str = 'self-center'):

    def try_login(app_model: AppModel) -> None:  # local function to avoid passing username and password as arguments
        try:
            supabase: SupabaseClient = get_client(app.storage.user.get('username'))
            access_token: str = app.storage.user.get('access_token', None)
            if access_token is None:
                res: AuthResponse = supabase.auth.sign_in_with_password({
                    "email": username.value,
                    "password": password.value
                })
                if not res:
                    ui.notify('Wrong username or invalid password', color='negative')
                else:
                    print("Thinking we have logged in and want to redirect after storage 1")
                    app.storage.user.update(
                        {
                            'username': username.value,
                            'user_id': res.user.id,
                            'access_token': res.session.access_token,
                            'refresh_token': res.session.refresh_token,
                            'profile': res.user.model_dump_json()
                        }
                    )
                    if app_model is None:
                        app_model = get_app_model(username.value)

                    response = supabase.table('personae').select('cv_resume').eq('owner', res.user.id).execute()
                    new_cv = None
                    if response is not None:
                        if len(response.data) > 0:
                            app_model.personae[0].cv_resume = TypeAdapter(resume_cv.Resume).validate_json(
                                response.data[0]['cv_resume'])
                            new_cv = app_model.personae[0].cv_resume
                    if new_cv is None:
                        app_model.personae[0].cv_resume = resume_cv.Resume(
                            field_schema="https://raw.githubusercontent.com/reorx/jsoncv/master/schema/jsoncv.schema.json",
                            basics=Basics(
                                profiles=[],
                                location=Location()
                            ),
                            work=[],
                            volunteer=[],
                            education=[],
                            awards=[],
                            certificates=[],
                            publications=[],
                            skills=[],
                            languages=[],
                            interests=[],
                            references=[],
                            projects=[],
                            meta=Meta(
                                canonical="https://raw.githubusercontent.com/reorx/jsoncv/master/schema/jsoncv.schema.json",
                                version="v2.0.0",
                                lastModified="2024-02-26T20:00:34+00:00Z"
                            )

                        )
                        data = supabase.table('personae').insert({
                            "cv_resume": app_model.personae[0].cv_resume.model_dump_json(),
                            "owner": res.user.id
                        }).execute()
                    app_model.bucket = get_user_storage_bucket(supabase, username.value)
                    ui.navigate.to(
                        app.storage.user.get('referrer_path', '/me'))  # go back to where the user wanted to go
            else:
                sess: Session = supabase.auth.get_session()
                if sess is not None:
                    try:
                        info = supabase.auth.get_user_info(sess.access_token)
                        if info is not None:
                            print("Thinking we have logged in and want to redirect after storage 2")
                            app.storage.user.update(
                                {
                                    'username': username.value,
                                    'user_id': sess.user.id,
                                    'access_token': sess.access_token,
                                    'profile': sess.user.model_dump_json()
                                }
                            )
                            response = supabase.table('personae').select('cv_resume').eq('owner',
                                                                                         sess.user.id).execute()
                            new_cv = None
                            if response is not None:
                                if len(response.data) > 0:
                                    app_model.personae[0].cv_resume = TypeAdapter(resume_cv.Resume).validate_json(
                                        response.data[0]['cv_resume'])
                                    new_cv = app_model.personae[0].cv_resume
                            if new_cv is None:
                                app_model.personae[0].cv_resume = resume_cv.Resume(
                                    field_schema="https://raw.githubusercontent.com/reorx/jsoncv/master/schema/jsoncv.schema.json",
                                    basics=Basics(
                                        profiles=[],
                                        location=Location()
                                    ),
                                    work=[],
                                    volunteer=[],
                                    education=[],
                                    awards=[],
                                    certificates=[],
                                    publications=[],
                                    skills=[],
                                    languages=[],
                                    interests=[],
                                    references=[],
                                    projects=[],
                                    meta=Meta(
                                        canonical="https://raw.githubusercontent.com/reorx/jsoncv/master/schema/jsoncv.schema.json",
                                        version="v2.0.0",
                                        lastModified="2024-02-26T20:00:34+00:00Z"
                                    )

                                )
                                data = supabase.table('personae').insert({
                                    "cv_resume": app_model.personae[0].cv_resume.model_dump_json(),
                                    "owner": sess.user.id
                                }).execute()

                            ui.navigate.to(
                                app.storage.user.get('referrer_path',
                                                     '/me'))  # go back to where the user wanted to go
                        else:
                            ui.notify('Expired session username or password', color='negative')
                    except AuthApiError as auth_api_error:
                        app.storage.user.clear()
                        ui.notify(auth_api_error.message, color='negative')
                else:
                    app.storage.user.clear()
                    ui.notify('No session -  failed.', color='negative')

        except AuthApiError as auth_api_error:
            app.storage.user.clear()
            ui.notify(auth_api_error.message, color='negative', position="center")
        except AuthInvalidCredentialsError as auth_api_error:
            app.storage.user.clear()
            ui.notify(auth_api_error.message, color='negative', position="center")
        except Exception as e:
            app.storage.user.clear()
            ui.notify(str(e), color="negative", position="center")

    if app.storage.user.get('access_token', None) is not None:
        return RedirectResponse('/me')

    def try_register() -> None:
        try:
            supabase: SupabaseClient = get_client(username.value)

            res = supabase.auth.sign_up({
                "email": username.value,
                "password": password.value
            })
            if res is not None:
                ui.notify('Please check your email to finish the sign up process', color="positive", position="center")
        except AuthApiError as auth_api_error:
            ui.notify(auth_api_error.message, color='negative', position="center")
        except AuthInvalidCredentialsError as auth_api_error:
            ui.notify(auth_api_error.message, color='negative', position="center")
        except Exception as e:
            ui.notify(str(e), color="negative", position="center")
    access_token = app.storage.user.get("access_token", None)
    if access_token is None:
        with ui.card().classes(f'{position_class} col col-6'):
            ui.image(f"images/logo.png")
            ui.label('Login or Sign Up').classes('self-center h2')
            username = ui.input('Username').on('keydown.enter', lambda: try_login(app_model)).classes("row w-full")
            password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', lambda: try_login(app_model)).classes("row w-full")
            with ui.card_actions().classes("row justify-between w-full"):
                ui.button('Log in', on_click=lambda: try_login(app_model))
                ui.button('Forgot password?', on_click=lambda: ui.navigate.to("/forgot")).props('color=warning')
                ui.button('Sign up', on_click=try_register).props('color=positive')
            with ui.card_actions().classes("column justify-center w-full"):
                ui.label('Note! The app is completely free to use for now')
    else:
        await reset_password_content(app_model)
    return None
