from fastapi import APIRouter, Depends,Form,File,UploadFile
from app.dtos.resumeParser import ResumeParserBase 
from app.dtos.profile import ProfileBase

router = APIRouter()

@router.post("/parse_resume", response_model=ProfileBase)
async def parse_resume(file: UploadFile = File(...),):
    
    
    return {"parsed_resume": resume_data.resume}

