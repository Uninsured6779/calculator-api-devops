from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "UP"
    }


def test_version():
    response = client.get("/version")

    assert response.status_code == 200
    assert "version" in response.json()


def test_addition():
    response = client.post(
        "/calculate",
        json={
            "a": 10,
            "b": 5,
            "operation": "add"
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_subtraction():
    response = client.post(
        "/calculate",
        json={
            "a": 10,
            "b": 5,
            "operation": "subtract"
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_multiplication():
    response = client.post(
        "/calculate",
        json={
            "a": 10,
            "b": 5,
            "operation": "multiply"
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 50


def test_division():
    response = client.post(
        "/calculate",
        json={
            "a": 10,
            "b": 5,
            "operation": "divide"
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 2


def test_division_by_zero():
    response = client.post(
        "/calculate",
        json={
            "a": 10,
            "b": 0,
            "operation": "divide"
        }
    )

    assert response.status_code == 400


def test_invalid_operation():
    response = client.post(
        "/calculate",
        json={
            "a": 10,
            "b": 5,
            "operation": "power"
        }
    )

    assert response.status_code == 400
