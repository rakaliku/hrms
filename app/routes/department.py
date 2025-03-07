from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..models.department import Department
from ..schemas.department import DepartmentCreate, DepartmentResponse
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.post("/departments/", response_model=DepartmentResponse, summary="Create Department", tags=["Department"])
def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    try:
        new_department = Department(**department.dict())
        db.add(new_department)
        db.commit()
        db.refresh(new_department)
        return new_department
    except IntegrityError as e:
        db.rollback()
        if "Duplicate entry" in str(e.orig):
            raise HTTPException(status_code=400, detail="Department Name already exist, entry not possible")
        else:
            raise HTTPException(status_code=500, detail="An error occurred")