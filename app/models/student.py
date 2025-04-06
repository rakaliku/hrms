from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    roll_number = Column(String(10), unique=True, nullable=False)

    # Relationships
    student_attendance = relationship("StudentAttendance", back_populates="students")