from pydantic import BaseModel, field_validator
from datetime import datetime

class AttendanceCreate(BaseModel):
    """AttendanceCreate model definition."""
    employee_id: int
    check_in: str  # Change to str for custom validation
    attendance_status: str

    @field_validator('check_in')
    def validate_check_in(cls, value):
        if isinstance(value, datetime):  # Already a datetime object, return as is
            return value
        try:
            return datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError('check_in must be in yyyy-mm-dd format')

class AttendanceUpdate(AttendanceCreate):
    """AttendanceUpdate model definition."""
    check_out: str  # Change to str for custom validation

    @field_validator('check_out')
    def validate_check_out(cls, value):
        try:
            return datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError('check_out must be in yyyy-mm-dd format')

class AttendanceResponse(AttendanceCreate):
    """AttendanceResponse model definition."""
    attendance_id: int
    employee_id: int
    check_in: datetime
    check_out: datetime | None = None
    attendance_status: str

    class Config:
        orm_mode = True


# class AttendanceCreate(BaseModel):
#     """AttendanceCreate model definition."""
#     employee_id: int
#     check_in : datetime
#     attendance_status: str
    

# class AttendanceUpdate(AttendanceCreate):
#     """AttendanceUpdate model definition."""
#     check_out: datetime


# class AttendanceReposne(AttendanceCreate):
#     """AttendanceReposne model definition."""
#     attendance_id: int
#     employee_id: int
