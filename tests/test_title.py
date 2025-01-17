import requests
from lib.config import BASE_URL


def test_1():
    response = requests.get(f"{BASE_URL}/title")
    response.raise_for_status()
    response_json = response.json()
    assert len(response_json["titles"]) > 0


def test_2():
    response = requests.get(f"{BASE_URL}/title/Ozymandias")
    response.raise_for_status()
    response_json = response.json()
    assert response_json[0]["title"] == "Ozymandias"


def test_3():
    response = requests.get(f"{BASE_URL}/title/spring/title")
    response.raise_for_status()
    response_json = response.json()
    assert all("spring" in response["title"].lower() for response in response_json)
    assert all(len(response) == 1 for response in response_json)


def test_4():
    response = requests.get(f"{BASE_URL}/title/In spring and summer winds may blow:abs/title")
    response.raise_for_status()
    response_json = response.json()
    assert all(response["title"] == "In spring and summer winds may blow" for response in response_json)
    assert all(len(response) == 1 for response in response_json)


def test_5():
    response = requests.get(f"{BASE_URL}/title/Ozymandias/author,title,linecount")
    response.raise_for_status()
    response_json = response.json()

    expected_fields = ['author', 'title', 'linecount']
    for response in response_json:
        assert response["title"] == "Ozymandias"
        for field in expected_fields:
            assert field in response

        assert len(response) == 3


def test_6():
    response = requests.get(f"{BASE_URL}/title/Ozymandias/title,lines.text")
    response.raise_for_status()
    response_list = response.text.split("\n")
    response_list = [x for x in response_list if x]
    assert response_list[0] == "title"
    assert response_list[1] == "Ozymandias"
    assert response_list[2] == "lines"
    assert len(response_list[3:]) > 0