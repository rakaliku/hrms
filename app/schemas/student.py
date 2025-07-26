from pydantic import BaseModel, field_validator


class StudentGet(BaseModel):
    """StudentGet model definition."""
    name: str
    email: str | None = None
    roll_number: str | None = None

    class Config:
        orm_mode = True


class StudentResponse(StudentGet):
    id: int
    class Config:
        orm_mode = True