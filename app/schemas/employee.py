from pydantic import BaseModel


class EmployeeBase(BaseModel):
    name : str
    department_id : int
    role_id : int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    class Config:
        orm_mode = True

