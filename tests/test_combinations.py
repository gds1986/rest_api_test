import requests
from lib.config import BASE_URL


def test_1():
    response = requests.get(f"{BASE_URL}/title,random/Sonnet;3")
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json) == 3
    assert all("Sonnet" in response["title"] for response in response_json)


def test_2():
    response = requests.get(f"{BASE_URL}/title,author,linecount/Winter;Shakespeare;18")
    response_json = response.json()
    assert response.status_code == 200
    assert all("Winter" in response["title"] for response in response_json)
    assert all("Shakespeare" in response["author"] for response in response_json)
    assert all(response["linecount"] == 18 for response in response_json)
