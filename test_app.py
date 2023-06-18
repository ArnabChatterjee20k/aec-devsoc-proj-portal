from fastapi.testclient import TestClient
from fastapi import status
from app import api

client = TestClient(app=api)

def test_docs_redirection():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK