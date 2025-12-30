import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home_page(client):
    """Test that the home page returns a 200 OK and correct JSON"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, DevOps World!"

def test_invalid_route(client):
    """Test that a non-existent route returns 404"""
    response = client.get('/non-existent')
    assert response.status_code == 404