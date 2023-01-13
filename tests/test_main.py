"""Test Main module."""

from fastapi.testclient import TestClient


def test_index(client: TestClient) -> None:
    """Must check index."""
    response = client.get('/')
    assert response.json() == {'message': 'Hello Template'}
