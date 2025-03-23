from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    subject = Column(String(50), nullable=False)

    # Relationships
    student_attendance = relationship("StudentAttendance", back_populates="classes")