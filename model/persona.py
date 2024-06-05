from typing import List, Optional
from pydantic import BaseModel, EmailStr

from model import resume_cv
from model.jobs import JobApplication


class Candidate(BaseModel):
    id: int
    name: str
    email: EmailStr
    cv_resume: resume_cv.Resume
    applications: Optional[List[JobApplication]]
