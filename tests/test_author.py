import requests
from lib.config import BASE_URL


def test_1():
    response = requests.get(f"{BASE_URL}/author")
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json["authors"]) > 0


def test_2():
    response = requests.get(f"{BASE_URL}/author/Ernest Dowson")
    response_json = response.json()
    assert response.status_code == 200
    assert all(response["author"] == "Ernest Dowson" for response in response_json)


def test_3():
    response = requests.get(f"{BASE_URL}/author/owson/author")
    response_json = response.json()
    assert response.status_code == 200
    assert all("owson" in response["author"] for response in response_json)
    assert all(len(response) == 1 for response in response_json)


def test_4():
    response = requests.get(f"{BASE_URL}/author/Ernest Dowson:abs/author")
    response_json = response.json()
    assert response.status_code == 200
    assert all(response["author"] == "Ernest Dowson" for response in response_json)
    assert all(len(response) == 1 for response in response_json)


def test_5():
    response = requests.get(f"{BASE_URL}/author/Ernest Dowson/author,title,linecount")
    response_json = response.json()
    assert response.status_code == 200

    expected_fields = ['author', 'title', 'linecount']
    for response in response_json:
        assert response["author"] == "Ernest Dowson"
        for field in expected_fields:
            assert field in response

        assert len(response) == 3

def test_6():
    response = requests.get(f"{BASE_URL}/author/Ernest Dowson/author,title,linecount.text")
    assert response.status_code == 200
    response_list = response.text.split("\n")
    response_list = [x for x in response_list if x]
    assert len(response_list) == 6
    assert response_list[0] == "title"
    assert response_list[2] == "author"
    assert response_list[4] == "linecount"