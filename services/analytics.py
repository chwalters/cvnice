from typing import Optional
from loguru import logger
from config import Settings

# Posthog is optional
try:
    from posthog import Posthog
except ImportError as ie:
    logger.info("Posthog support is not enabled")


class Analytics:
    def __init__(self):
        self.reporter = None

    def capture(self, distinct_id: str, event: str, properties: Optional[dict] = None) -> None:
        pass


class PosthogAnalytics(Analytics):
    def __init__(self, settings: Settings):
        super().__init__()
        try:
            if settings.posthog_api_url is not None and len(
                    settings.posthog_api_url) > 0 and settings.posthog_api_key is not None and len(
                    settings.posthog_api_key) > 0:
                self.reporter = Posthog(project_api_key=settings.posthog_api_key, host=settings.posthog_api_url)
        except:
            self.reporter = None

    def capture(self, distinct_id: str, event: str, properties: Optional[dict] = None) -> None:
        if self.reporter is not None:
            self.reporter.capture(distinct_id, event, properties)
