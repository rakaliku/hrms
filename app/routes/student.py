from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..models.student import Student
from ..schemas.student import StudentGet


router = APIRouter()

@router.get("/students/", response_model=list[StudentGet])
async def get_students(db: Session = Depends(get_db)):
    """Get all students."""
    students = db.query(Student).all()
    return students