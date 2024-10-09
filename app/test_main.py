from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_get_xml():
    response = client.get("/api/rates?from=USD&to=RUB&value=1")
    assert response.status_code == 200
