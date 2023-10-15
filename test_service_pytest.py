import requests

BASE_URL_SERVER1 = "http://localhost:5000/analyze_paragraph/"
BASE_URL_SERVER2 = "http://localhost:5001/"


def test_server1_positive_sentiment():
    response = requests.post(BASE_URL_SERVER1, json={"text": "I love this product. It is amazing."})
    data = response.json()
    assert data["label"] == "POSITIVE"
    assert 0.5 < data["score"] <= 1.0


def test_server1_negative_sentiment():
    response = requests.post(BASE_URL_SERVER1, json={"text": "I hate this. It's terrible."})
    data = response.json()
    assert data["label"] == "NEGATIVE"
    assert 0.5 < data["score"] <= 1.0


def test_server2_positive_sentiment():
    response = requests.post(BASE_URL_SERVER2, json={"text": "This is fantastic!"})
    data = response.json()
    assert data["label"] == "POSITIVE"
    assert 0.5 < data["score"] <= 1.0


def test_server2_negative_sentiment():
    response = requests.post(BASE_URL_SERVER2, json={"text": "This is not good at all."})
    data = response.json()
    assert data["label"] == "NEGATIVE"
    assert 0.5 < data["score"] <= 1.0
