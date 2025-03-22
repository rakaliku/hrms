from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)

def test_check_in():
    response = client.post("/attendance/checkin", json={
        "employee_id": 1,
        "check_in": "2023-10-01",
        "attendance_status": "In"
    })
    assert response.status_code == 200
    assert response.json()["check_in"] == datetime.strptime("2023-10-01", '%Y-%m-%d')

def test_check_out():
    response = client.put("/attendance/checkout/1", json={
        "check_out": "2023-10-01"
    })
    assert response.status_code == 200
    assert response.json()["check_out"] == datetime.strptime("2023-10-01", '%Y-%m-%d')

def test_get_attendance_by_date():
    response = client.get("/attendance/date/2023-10-01")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
