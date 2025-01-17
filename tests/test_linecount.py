import requests
from lib.config import BASE_URL


def test_1():
    response = requests.get(f"{BASE_URL}/linecount/3")
    response.raise_for_status()
    response_json = response.json()
    assert all(len(response["lines"]) == 3 for response in response_json)
    assert all(response["linecount"] == 3 for response in response_json)