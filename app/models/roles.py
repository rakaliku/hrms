from sqlalchemy import Column, Integer, String, ForeignKey
from ..core.database import Base

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))