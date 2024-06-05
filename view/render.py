import json
import tempfile
from pathlib import Path
from typing import Optional

from carbone_sdk import carbone_sdk
from loguru import logger
from storage3.utils import StorageException

from model.application import AppModel
from model.resume_cv import Resume
from config import settings
from supabase import Client as SupabaseClient

class TemplateRenderer:

    def __init__(self, app_model: AppModel):
        super().__init__()
        self.app_model = app_model
        self.csdk = carbone_sdk.CarboneSDK(settings.carbone_access_token)

    def default_template_path(self, document_type: str) -> Optional[str]:
        template_path: Optional[str] = None
        if document_type == "cv":
            template_path = "appdata/templates/simple_cv.docx"
            logger.debug(f"No template name provided, using {template_path}")
        else:
            template_path = "appdata/templates/simple_cover.docx"
            logger.debug(f"No template name provided, using {template_path}")
        return template_path

    def render(self,
               payload: dict,
               template_name: Optional[str],
               username: str,
               supabase: SupabaseClient,
               document_type="cv",
               format: str = "docx") -> Optional[str]:
        carbone_data = dict(data=payload, convertTo=format)
        logger.debug(carbone_data)
        template_path: Optional[str] = None
        output_path: Optional[str] = None
        if template_name is not None:
            try:
                stem_prefix = Path(template_name).stem
                stem_suffix = Path(template_name).suffix
                with tempfile.NamedTemporaryFile(prefix=stem_prefix, suffix=stem_suffix, delete=False) as tmp_fp:
                    named_temp_file = tmp_fp.file.name
                    res = supabase.storage.from_(username).download(template_name)
                    fd = open(named_temp_file, "wb")
                    fd.write(res)
                    fd.close()
                    template_path = str(Path(named_temp_file))
            except StorageException as se:
                logger.error(se)

        if template_path is None:
            template_path = self.default_template_path(document_type)

        try:
            # First, download custom template with name or if None use default
            logger.debug(f"Rendering template: {template_path}")
            report_bytes, unique_report_name = self.csdk.render(
                template_path,
                carbone_data
            )
            # Create the local file
            stem_prefix = Path(template_path).stem
            with tempfile.NamedTemporaryFile(prefix=stem_prefix, suffix=f".{format}", delete=False) as tmp_fp:
                named_temp_file = tmp_fp.file.name
                fd = open(named_temp_file, "wb")
                fd.write(report_bytes)
                fd.close()
                output_path = Path(named_temp_file)

        except Exception as err:
            logger.error(err)
            logger.error(f"Can't create carbone output for {template_name}")

        return output_path