from sqlalchemy import Column, Integer, Float, ForeignKey
from ..core.database import Base
from sqlalchemy.orm import relationship

class Salary(Base):
    __tablename__ = "salaries"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    amount = Column(Float)
    employee = relationship("Employee", back_populates="salary")