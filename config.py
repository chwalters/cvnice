from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    gemini_api_key: str
    nicegui_storage_secret: str
    dev_mode: str
    carbone_access_token: str
    supabase_url: str
    supabase_key: str
    supabase_jwt_secret: str
    sentry_dsn: str
    posthog_api_key: str
    posthog_api_url: str

settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
