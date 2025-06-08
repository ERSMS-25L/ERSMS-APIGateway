import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_ready():
    res = client.get("/ready")
    assert res.status_code == 200
    assert res.json() == {"status": "ready"}

def test_user_forwarding():
    res = client.get("/user/1")
    assert res.status_code in (200, 502)  # 200 si user-service está levantado, 502 si no
    if res.status_code == 200:
        assert "user_id" in res.json()

def test_task_forwarding():
    payload = {
        "title": "Test task",
        "description": "API Gateway test",
        "due_date": "2025-06-08"
    }
    res = client.post("/task/create", json=payload)
    assert res.status_code in (200, 502)
    if res.status_code == 200:
        assert "title" in res.json()
