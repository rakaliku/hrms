from fastapi import FastAPI
from app.routes import department, employee, attendance
from app.core.database import create_tables

app = FastAPI()
create_tables() # We can run this at the very first time just to create the required tables


app.include_router(department.router)
app.include_router(employee.router)
app.include_router(attendance.router)

@app.get("/")
def main_func():
    return {"message" : "hrms portal"}

