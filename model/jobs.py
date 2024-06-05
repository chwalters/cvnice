from typing import List, Optional

from email_validator import validate_email, EmailNotValidError
from loguru import logger
from pydantic import BaseModel, EmailStr, HttpUrl, Field, ConfigDict, field_validator
from datetime import datetime
from enum import Enum

from model.resume_cv import Resume


class HiringManager(BaseModel):

    @field_validator('email', mode='before', check_fields=False)
    def empty_email_to_none(cls, v):
        if v == '' or v == 'None' or v is None:
            logger.debug(f"{v} is empty")
            return None
        else:
            try:
                validate_email(v)
                return v
            except EmailNotValidError as e:
                return None

    name: str
    email: Optional[EmailStr]
    phone: Optional[str]


class JobType(Enum):
    FULL_TIME = "Full Time"
    PART_TIME = "Part Time"
    CONTRACT = "Contractor"
    INTERN = "Intern"
    APPRENTICE = "Apprentice",
    OTHER = "Other"


class WorkMode(Enum):
    REMOTE = "Remote"
    ONSITE = "Onsite"
    HYBRID = "Hybrid"
    OTHER = "Other"


class JobOpening(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    id: Optional[int] = Field(None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    title: str
    company: str
    description: Optional[str]
    location: str
    url: Optional[HttpUrl] = Field(None)
    hiring_manager: Optional[HiringManager] = None
    job_type: Optional[JobType] = None
    work_mode: Optional[WorkMode] = None
    keywords: Optional[str] = Field(None)
    owner: Optional[str] = None

class JobApplication(BaseModel):
    id: int
    job_opening: JobOpening
    submitted: bool
    submission_date: Optional[datetime] = None
    submission_confirmation_number: Optional[str] = None
    cover_letter: str
    job_interview_date: Optional[datetime] = None
    job_offered: Optional[bool] = None
    job_accepted: Optional[bool] = None
    cv_template: Optional[str] = None
    cv: Optional[Resume] = None