"""Main Conftest."""

import pytest
from fastapi.testclient import TestClient

from src.main import create_app


@pytest.fixture
def client() -> TestClient:
    """Client Fixture."""
    with TestClient(create_app()) as client:
        yield client
