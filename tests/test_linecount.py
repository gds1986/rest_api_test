import requests
from lib.config import BASE_URL


def test_1():
    response = requests.get(f"{BASE_URL}/linecount/3")
    response_json = response.json()
    assert response.status_code == 200
    assert all(len(response["lines"]) == 3 for response in response_json)
    assert all(response["linecount"] == 3 for response in response_json)