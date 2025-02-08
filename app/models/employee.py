from sqlalchemy import Column, Integer, String, ForeignKey
from ..core.database import Base
from sqlalchemy.orm import relationship
# from ..models import salary, leave

class Employee(Base):
    __tablename__="employees"
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(100), index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))
    
    salary = relationship("Salary", back_populates="employee") 
    leaves = relationship("Leave", back_populates="employee")
    attendances = relationship("Attendance", back_populates="employee")