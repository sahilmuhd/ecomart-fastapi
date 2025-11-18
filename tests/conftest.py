# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def sample_data():
    return {
        "name": "Sample Store",
        "description": "A sample store for testing",
        "owner": "test_user"
    }