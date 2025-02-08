from sqlalchemy import Column, Integer, String, ForeignKey
from ..core.database import Base
from sqlalchemy.orm import relationship

class Leave(Base):
    __tablename__ = "leaves"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    reason = Column(String(500))
    status = Column(String(10), default="Pending")
    employee = relationship("Employee", back_populates="leaves")