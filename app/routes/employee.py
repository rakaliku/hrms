from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..models.employee import Employee
from ..models.roles import Role
from ..schemas.employee import EmployeeCreate, EmployeeResponse

router =APIRouter()

@router.post("/employee/", response_model=EmployeeResponse)
async def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == employee.role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Invalid Role ID, Role not found")
    new_employee = Employee(**employee.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee
