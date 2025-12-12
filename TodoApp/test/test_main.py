from fastapi.testclient import TestClient
from ..main import app
from fastapi import status


client = TestClient(app)


def test_return_health_check():
    respone = client.get("/healthy")
    assert respone.status_code == status.HTTP_200_OK
    assert respone.json() == {"status": "Healthy"}