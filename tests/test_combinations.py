import requests
from lib.config import BASE_URL


def test_1():
    response = requests.get(f"{BASE_URL}/title,random/Sonnet;3")
    response.raise_for_status()
    response_json = response.json()
    assert len(response_json) == 3
    assert all("Sonnet" in response["title"] for response in response_json)


def test_2():
    response = requests.get(f"{BASE_URL}/title,author,linecount/Winter;Shakespeare;18")
    response.raise_for_status()
    response_json = response.json()
    assert all("Winter" in response["title"] for response in response_json)
    assert all("Shakespeare" in response["author"] for response in response_json)
    assert all(response["linecount"] == 18 for response in response_json)
