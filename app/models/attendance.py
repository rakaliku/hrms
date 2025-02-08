from sqlalchemy import Column, DateTime, Integer, ForeignKey, String, text
from sqlalchemy.orm import relationship
from ..core.database import Base
from datetime import datetime


class Attendance(Base):
    __tablename__ = "attendances"
    attendance_id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    check_in = Column(DateTime,default=datetime.utcnow)
    check_out = Column(DateTime, nullable=True)
    attendance_status = Column(String(20), default="In", server_default=text("'In'"))
    employee = relationship("Employee",back_populates="attendances")
