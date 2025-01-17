import requests
from lib.config import BASE_URL


def test_1():
    response = requests.get(f"{BASE_URL}/author,poemcount/Dickinson;2")
    response.raise_for_status()
    response_json = response.json()
    assert all("Dickinson" in response["author"] for response in response_json)
    assert len(response_json) == 2


def test_2():
    response = requests.get(f"{BASE_URL}/author,poemcount/Dickinson;2/author,title,linecount")
    response.raise_for_status()
    response_json = response.json()

    expected_fields = ['author', 'title', 'linecount']
    for response in response_json:
        for field in expected_fields:
            assert field in response

        assert len(response) == 3