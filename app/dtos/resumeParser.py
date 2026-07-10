from typing import Optional
from pydantic import BaseModel
class ResumeParserBase(BaseModel):
    resume: Optional[str] = None

    