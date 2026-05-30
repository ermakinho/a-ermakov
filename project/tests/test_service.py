from fastapi.testclient import TestClient
from src.service.app import app

client = TestClient(app)


def make_valid_payload():
    return {
        "datetime": "2012-12-31 17:00:00",
        "season": 4,
        "holiday": 0,
        "workingday": 1,
        "weather": 2,
        "temp": 15.5,
        "atemp": 17.0,
        "humidity": 65,
        "windspeed": 12.5,
    }


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["service"] == "Bike Sharing Demand Predictor"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["model_loaded"] is True


def test_predict_endpoint_valid_request():
    response = client.post(
        "/predict",
        json=make_valid_payload(),
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_demand" in data
    assert isinstance(data["predicted_demand"], int)
    assert data["predicted_demand"] >= 0


def test_predict_endpoint_invalid_request():
    payload = make_valid_payload()
    payload["humidity"] = 150

    response = client.post(
        "/predict",
        json=payload,
    )

    assert response.status_code == 422