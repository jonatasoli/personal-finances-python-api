"""Test Main module."""

from datetime import datetime

from fastapi.testclient import TestClient


def test_index(client: TestClient) -> None:
    """Must check index."""
    response = client.get('/')
    assert response.json() == {'message': 'Hello Template'}


def test_create_record(client: TestClient) -> None:
    """Must return record created."""
    now = datetime.now()
    date_time = now.strftime('%m/%d/%Y')
    data_record = dict(
        id=1,
        user_id=1,
        account_id=1,
        category_id=1,
        type='debit',
        amount=10.0,
        date=date_time,
        description='one description',
    )
    response = client.post('/record', json=data_record)
    response_dict = response.json()
    response_dict.pop('note')
    response_dict.pop('tags')
    assert response_dict == data_record


def test_update_record(client: TestClient) -> None:
    """Must return record updated."""
    now = datetime.now()
    date_time = now.strftime('%m/%d/%Y')
    data_record = dict(
        id=1,
        user_id=1,
        account_id=1,
        category_id=1,
        type='debit',
        amount=10.0,
        date=date_time,
        description='one description',
    )
    response = client.put('/record', json=data_record)
    response_dict = response.json()
    response_dict.pop('note')
    response_dict.pop('tags')
    assert response_dict == data_record


def test_get_records(client: TestClient) -> None:
    """Must return save records."""
    response = client.get('/records')
    response_dict = response.json()
    assert len(response_dict) == 2
