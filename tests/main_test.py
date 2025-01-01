from fastapi.testclient import TestClient
from main import app

# Initialize TestClient
client = TestClient(app)

def test_read_root_status_code():
    """
    Test if the root endpoint ("/") returns a 200 status code.
    """
    response = client.get("/")
    assert response.status_code == 200

def test_read_root_response_content():
    """
    Test if the root endpoint ("/") returns the correct JSON response.
    """
    response = client.get("/")
    assert response.json() == {"message": "Welcome to FastAPI"}

def test_read_root_invalid_method():
    """
    Test if accessing the root endpoint with an unsupported method returns 405.
    """
    response = client.post("/")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}
