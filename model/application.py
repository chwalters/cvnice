from typing import Optional, List

from pydantic import BaseModel
from storage3.types import CreateOrUpdateBucketOptions

from model import resume_cv
from model.app_settings import AppSettings
from model.jobs import JobOpening, HiringManager, JobType, WorkMode
from model.persona import Candidate
from loguru import logger
from supabase import Client as SupabaseClient

app_models = {}

class AppModel(BaseModel):
    settings: Optional[AppSettings] = None
    personae: Optional[List[Candidate]] = None
    jobs: Optional[List[JobOpening]] = None
    bucket: Optional[dict] = None

def get_app_model(username: str) -> AppModel:
    # logger.info(f"Fetching app model for {username}")
    app_model: Optional[AppModel] = app_models.get(username, None)
    if app_model is None:
        # logger.info(f"No app_model for {username}, creating one")
        app_model = AppModel()
        cv: resume_cv.Resume = resume_cv.Resume()  # TypeAdapter(resume_cv.Resume).validate_json(my_default_cv_json)
        # my_default_cv_json = open("appdata/me.json").read()
        app_model: AppModel = AppModel()
        app_model.settings = AppSettings()
        app_model.jobs = [
            JobOpening(
                id=1,
                title="*Paste into job offer above for AI recognition*",
                company="",
                description="""
                """,
                location="",
                url=None,
                hiring_manager=HiringManager(
                    name="",
                    email=None,
                    phone=""
                ),
                job_type=JobType.FULL_TIME,
                work_mode=WorkMode.REMOTE,
                keywords="",
                owner=None
            )
        ]
        app_model.personae = [
            Candidate(
                id=0,
                name="Default User",
                email="default@email.com",
                cv_resume=cv,
                applications=None
            )
        ]
        app_models[username] = app_model
    else:
        pass
        # logger.info(f"Using existing app_model for {username}")

    return app_model

def get_user_storage_bucket(supabase: SupabaseClient, username: str) -> Optional[dict]:
    user_bucket: Optional[dict] = None
    if username is not None and len(username) > 0:
        if supabase is not None:
            try:
                user_bucket = supabase.storage.get_bucket(username)
            except Exception as e:
                logger.error(e)
                user_bucket = None

            if not user_bucket:
                try:
                    options: CreateOrUpdateBucketOptions = CreateOrUpdateBucketOptions(
                        public=False,
                        file_size_limit='10MB'
                    )
                    user_bucket = supabase.storage.create_bucket(username, options=options)
                except Exception as e:
                    logger.error(e)
                    user_bucket = None
    return user_bucket
