from pydantic import BaseModel
from datetime import datetime


class AttendanceCreate(BaseModel):
    """AttendanceCreate model definition."""
    employee_id: int
    check_in : datetime
    attendance_status: str
    

class AttendanceUpdate(AttendanceCreate):
    """AttendanceUpdate model definition."""
    check_out: datetime


class AttendanceReposne(AttendanceCreate):
    """AttendanceReposne model definition."""
    attendance_id: int
    employee_id: int
    check_in : datetime
    check_out : datetime | None = None
    attendance_status : str


    class Config:
        orm_mode = True
