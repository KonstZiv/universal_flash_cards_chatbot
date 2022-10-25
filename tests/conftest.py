from app.main import app

from fastapi.testclient import TestClient

import pytest


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)
