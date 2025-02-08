# HRMS FastAPI Application

This is a Human Resource Management System (HRMS) built using **FastAPI**. The application helps manage employee information, roles, attendance tracking, and leave management.

## Features
- Employee Management  
- Role-Based Access Control  
- Attendance Tracking (with Check-In/Check-Out logic)  
- Leave Management  
- Salary Details Tracking  

## Tech Stack
- **Backend**: FastAPI, SQLAlchemy  
- **Database**: MySQL  
- **Authentication**: JWT (if applicable)  
- **Deployment**: cPanel (Python App)  

## Prerequisites
- Python 3.8+
- MySQL Database  
- Virtual Environment (`venv`)  

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/hrms_fastapi.git
   cd hrms_fastapi
   ```

2. Create and activate a virtual environment:  
   ```bash
   python -m venv hrmsvenv
   hrmsvenv\Scripts\activate  # Windows
   source hrmsvenv/bin/activate  # Linux/Mac
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database in `config.py` with your MySQL connection details.

5. Run the application:  
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

6. Access the application at:  
   `http://127.0.0.1:8000`  

7. API documentation is available at:  
   - Swagger UI: `http://127.0.0.1:8000/docs`  
   - Redoc: `http://127.0.0.1:8000/redoc`  

## Project Structure
```
hrms_fastapi/
├── app/
│   ├── core/               # Database and Config files
│   ├── models/             # SQLAlchemy models (Employee, Department, etc.)
│   ├── routes/             # API routes for different modules
│   └── main.py             # FastAPI application entry point
├── hrmsvenv/               # Virtual environment (not pushed to Git)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Deployment on cPanel
1. Zip the project and upload it to cPanel's **File Manager**.  
2. Use **Setup Python App** in cPanel to create a virtual environment.  
3. Set the application startup file and entry point:  
   - **Application root**: `/home2/username/public_html/dev/hrms_fastapi`  
   - **Application startup file**: `app/main.py`  
   - **Application entry point**: `app`  
4. Install dependencies in the cPanel virtual environment:  
   ```bash
   pip install -r requirements.txt
   ```

## License
This project is licensed under the MIT License.

