import requests
from lib.config import BASE_URL


def test_1():
    response = requests.get(f"{BASE_URL}/random/3")
    response.raise_for_status()
    response_json = response.json()
    assert len(response_json) == 3


def test_2():
    response = requests.get(f"{BASE_URL}/random/3/author,title,linecount")
    response.raise_for_status()
    response_json = response.json()

    expected_fields = ['author', 'title', 'linecount']
    for response in response_json:
        for field in expected_fields:
            assert field in response

        assert len(response) == 3