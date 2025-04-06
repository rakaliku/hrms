"""
main.py - Entry point for the HRMS FastAPI application.

This module initializes the FastAPI app and defines basic routes for the application.
"""


from fastapi import FastAPI
from app.routes import department, employee, attendance, student
from app.core.database import create_tables
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
create_tables() # We can run this at the very first time just to create the required tables


app.include_router(department.router)
app.include_router(employee.router)
app.include_router(attendance.router)
app.include_router(student.router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Change "*" to ["http://localhost:3000"] for React frontend in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def main_func():
    """Main function of mrms app"""
    return {"message" : "hrms portal"}
