from fastapi import APIRouter, HTTPException, Depends

from ..models.attendance import Attendance
from ..schemas.attendance import *
from ..core.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime, timedelta


router = APIRouter()


@router.post("/attendance/checkin", response_model=AttendanceResponse)
def check_in(attendance: AttendanceCreate, db: Session= Depends(get_db)):
    new_attendance = Attendance(
        employee_id=attendance.employee_id,
        check_in= attendance.check_in,
        attendance_status = "In"
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance

@router.put("/attendance/checkout/{employee_id}", response_model=AttendanceResponse)
def check_out(employee_id:int, attendance_data: AttendanceUpdate, db: Session = Depends(get_db)):
    #attendance_record = db.query(Attendance).filter(Attendance.attendance_id == attendance_id).first()
    attendance_record =(
        db.query(Attendance)
        .filter(Attendance.employee_id == employee_id, Attendance.check_out == None)
        .order_by(Attendance.check_in.desc())
        .first()
    )
    print("Attendance record--",attendance_record)
    if not attendance_record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    if attendance_record.check_out:
        raise HTTPException(status_code=400, detail="Attendance record already checked out")
    

    attendance_record.check_out = datetime.utcnow()
    attendance_record.attendance_status = "Out"
    db.commit()
    db.refresh(attendance_record)
    return attendance_record



@router.get("/attendance/{employee_id}", response_model=list[AttendanceResponse])
def get_attendance(employee_id: int, db: Session = Depends(get_db)):
    attendance_record = db.query(Attendance).filter(Attendance.employee_id == employee_id).all()
    if not attendance_record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance_record


# @router.get("/attendance/date/{date}", response_model=list[AttendanceResponse])
# def get_attendance_by_date(date: str, db: Session = Depends(get_db)):
#     parsed_date = datetime.strptime(date, '%Y-%m-%d')
#     start_date = parsed_date.replace(hour=0, minute=0, second=0, microsecond=0)
#     end_date = start_date+timedelta(days=1)
#     print("Querying for date range",start_date, end_date)
#     attendance_record = db.query(Attendance).filter(Attendance.check_in >= start_date, Attendance.check_in < end_date).all()
#     if not attendance_record:
#         raise HTTPException(status_code=404, detail="Attendance record not found")
#     return attendance_record

@router.get("/attendance", response_model=list[AttendanceResponse])
def get_all_attendance(db: Session = Depends(get_db)):
    return db.query(Attendance).all()