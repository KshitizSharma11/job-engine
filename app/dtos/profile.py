from typing import Optional, List, str,int
from pydantic import BaseModel
class ProfileBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    experience: Optional[int] = 0
    address: Optional[str] = None
    skills: Optional[List[str]] = []
    experience: Optional[int] = 0
    location: Optional[str] = None
    preferred_location: Optional[List[str]] = None
    resume : Optional[str] = None
