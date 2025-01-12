import requests
from lib.config import BASE_URL


def test_1():
    response = requests.get(f"{BASE_URL}/random/3")
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json) == 3


def test_2():
    response = requests.get(f"{BASE_URL}/random/3/author,title,linecount")
    response_json = response.json()
    assert response.status_code == 200

    expected_fields = ['author', 'title', 'linecount']
    for response in response_json:
        for field in expected_fields:
            assert field in response

        assert len(response) == 3