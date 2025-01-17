import requests
from lib.config import BASE_URL


def test_1():
    response = requests.get(f"{BASE_URL}/author")
    response.raise_for_status()
    response_json = response.json()
    assert len(response_json["authors"]) > 0


def test_2():
    response = requests.get(f"{BASE_URL}/author/Ernest Dowson")
    response.raise_for_status()
    response_json = response.json()
    assert all(response["author"] == "Ernest Dowson" for response in response_json)


def test_3():
    response = requests.get(f"{BASE_URL}/author/owson/author")
    response.raise_for_status()
    response_json = response.json()
    assert all("owson" in response["author"] for response in response_json)
    assert all(len(response) == 1 for response in response_json)


def test_4():
    response = requests.get(f"{BASE_URL}/author/Ernest Dowson:abs/author")
    response.raise_for_status()
    response_json = response.json()
    assert all(response["author"] == "Ernest Dowson" for response in response_json)
    assert all(len(response) == 1 for response in response_json)


def test_5():
    response = requests.get(f"{BASE_URL}/author/Ernest Dowson/author,title,linecount")
    response.raise_for_status()
    response_json = response.json()

    expected_fields = ['author', 'title', 'linecount']
    for response in response_json:
        assert response["author"] == "Ernest Dowson"
        for field in expected_fields:
            assert field in response

        assert len(response) == 3

def test_6():
    response = requests.get(f"{BASE_URL}/author/Ernest Dowson/author,title,linecount.text")
    response.raise_for_status()
    response_list = response.text.split("\n")
    response_list = [x for x in response_list if x]
    assert len(response_list) == 6
    assert response_list[0] == "title"
    assert response_list[2] == "author"
    assert response_list[4] == "linecount"