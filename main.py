from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from nicegui import app

from services.analytics import PosthogAnalytics

# Sentry is optional
try:
    import sentry_sdk
except ImportError as ie:
    logger.info("Sentry.io support is not enabled")


from config import settings
from view import frontend

if settings.sentry_dsn is not None:
    sentry_sdk.init(
        dsn=settings.sentry_dsn,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )

analytics: PosthogAnalytics = PosthogAnalytics(settings)

analytics.capture("application", "boot")

fast_app = FastAPI()


fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return dict(status="running")

logger.info("Initializing front end...")
frontend.init(fast_app, settings, analytics)

