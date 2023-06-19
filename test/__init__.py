from api.v1 import build_api
from fastapi.testclient import TestClient
api = build_api()
test_client = TestClient(app=api)