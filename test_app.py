from fastapi.testclient import TestClient
from fastapi import status
from app import api
from utils.auth import create_access_token , decode_access_token , get_password_hash , verify_password

client = TestClient(app=api)

def test_docs_redirection():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK

def test_create_access_token():
    subject = "user123"
    token = create_access_token(subject)
    assert isinstance(token, str)

def test_decode_access_token():
    token = create_access_token("test_")
    payload = decode_access_token(token)
    assert isinstance(payload, dict)
    assert "sub" in payload

def test_verify_password():
    plain_password = "password123"
    hashed_password = get_password_hash(plain_password)
    result = verify_password(plain_password, hashed_password)
    assert result is True

def test_get_password_hash():
    plain_password = "password123"
    hashed_password = get_password_hash(plain_password)
    assert isinstance(hashed_password, str)