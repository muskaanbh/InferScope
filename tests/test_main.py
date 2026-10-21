from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_generate_empty_prompt():
    response = client.post("/generate", json={"prompt": ""})

    assert response.status_code == 422


def test_generate_mocked():
    with patch("main.generate_text") as mock_generate:
        # define what our fake LLM will return
        mock_generate.return_value = {"response": "Hello from mock LLM"}
        # send a prompt to FastAPI endpoint
        response = client.post("/generate", json={"prompt": "Hello"})
        mock_generate.assert_awaited_once_with("Hello", "http://localhost:8001")
        # validate what FastAPI returns to client
        assert response.json() == {"response": "Hello from mock LLM"}
        
