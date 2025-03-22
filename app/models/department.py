from sqlalchemy import Column, Integer, String
from ..core.database import Base

class Department(Base):
    __tablename__="departments"
    id = Column(Integer,primary_key=True, index=True) # Its Auto increment column
    name = Column(String(100), unique=True, index=True)

    