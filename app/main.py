"""
main.py - Entry point for the HRMS FastAPI application.

This module initializes the FastAPI app and defines basic routes for the application.
"""


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
    """Main function of mrms app"""
    return {"message" : "hrms portal"}
