from pydantic import BaseModel, ConfigDict

class DepartmentCreate(BaseModel):
    name: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Human Resources"
            }
        }
    )

class DepartmentResponse(DepartmentCreate):
    id: int
    class Config:
        orm_mode = True

    