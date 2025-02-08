from fastapi import APIRouter, HTTPException, Depends

from ..models.attendance import Attendance
from ..schemas.attendance import *
from ..core.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime


router = APIRouter()


@router.post("/attendance/checkin", response_model=AttendanceReposne)
def check_in(attendance: AttendanceCreate, db: Session= Depends(get_db)):
    new_attendance = Attendance(
        employee_id=attendance.employee_id,
        check_in=attendance.check_in,
        attendance_status = "In"
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance

@router.put("/attendance/checkout/{attendance_id}", response_model=AttendanceReposne)
def check_out(attendance_id:int, attendance_data: AttendanceUpdate, db: Session = Depends(get_db)):
    attendance_record = db.query(Attendance).filter(Attendance.attendance_id == attendance_id).first()
    if not attendance_record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    if attendance_record.check_out:
        raise HTTPException(status_code=400, detail="Attendance record already checked out")
    

    attendance_record.check_out = attendance_data.check_out
    db.commit()
    db.refresh(attendance_record)
    return attendance_record



@router.get("/attendance/{employee_id}", response_model=list[AttendanceReposne])
def get_attendance(employee_id: int, db: Session = Depends(get_db)):
    attendance_record = db.query(Attendance).filter(Attendance.employee_id == employee_id).all()
    if not attendance_record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance_record