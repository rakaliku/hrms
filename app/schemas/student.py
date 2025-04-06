from pydantic import BaseModel, field_validator


class StudentGet(BaseModel):
    """StudentGet model definition."""
    student_id: int
    name: str
    age: int
    email: str | None = None

    class Config:
        orm_mode = True
        # arbitrary_types_allowed = True