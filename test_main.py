from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_courses():
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_course():
    response = client.get("/courses/Highlights of Calculus")
    assert response.status_code == 200
    assert response.json()['name'] == "Highlights of Calculus"

def test_get_chapter():
    response = client.get("/courses/Highlights of Calculus/chapters/Big Picture of Calculus")
    assert response.status_code == 200
    assert response.json()['name'] == "Big Picture of Calculus"

def test_rate_chapter():
    response = client.post("/courses/Highlights of Calculus/chapters/Big Picture of Calculus/rate", json={"rating": 1})
    assert response.status_code == 200
    assert response.json()['message'] == "Rating submitted successfully"
