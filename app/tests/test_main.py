# import pytest
# from fastapi import FastAPI
# from httpx import AsyncClient
# from app.main import app  # Import your FastAPI app instance

# @pytest.mark.asyncio
# async def test_read_main():
#     async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
#         response = await client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "hrms portal"}
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app instance

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hrms portal"}
