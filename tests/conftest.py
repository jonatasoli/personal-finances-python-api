import pytest
from fastapi.testclient import TestClient

from src.main import create_app


@pytest.fixture
def client():
    with TestClient(create_app()) as client:
        yield client
