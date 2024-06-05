from pydantic import BaseModel

class AppSettings(BaseModel):
    dark_mode: bool = False
    nomenclature: str = "CV"
    last_tab: str = "Basics"
    last_editor: str = "Form View"
    last_splitter: float = 20.0
    app_version: str = "0.0.8"
    license_info: str = "Open Source MIT License"
