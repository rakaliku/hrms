from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class StudentAttendance(Base):
    __tablename__ = "student_attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(10), nullable=False)  # e.g., "present", "absent", "late"

    # Relationships
    student = relationship("Student", back_populates="student_attendance")
    class_ = relationship("Class", back_populates="student_attendance")