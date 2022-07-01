from mock import patch
from fastapi.testclient import TestClient

from main import app


test_client = TestClient(app)


TEST_FLIGHT_ID: str = "A12"
TEST_OUTPUT_FILE_NAME: str = "test_file_pytest.csv"

# test with: python -m pytest tests


def test_get_flight_info():
    response = test_client.get(f"/flight/{TEST_FLIGHT_ID}")

    assert response.status_code == 200

    json_response = response.json()

    assert json_response["flight ID"] == TEST_FLIGHT_ID


@patch("routers.flights.OUTPUT_FILE_NAME", TEST_OUTPUT_FILE_NAME)
def test_write_flight_Info():
    test_data = {"Arrival": "test", "Departure": "test", "success": "test"}
    response = test_client.post(f"/flight/{TEST_FLIGHT_ID}", json=test_data)

    assert response.status_code == 200

    json_response = response.json()

    assert json_response["flight ID"] == TEST_FLIGHT_ID
    assert json_response["Arrival"] == test_data["Arrival"]
    assert json_response["Departure"] == test_data["Departure"]
    assert json_response["success"] == test_data["success"]
