"""Main module."""

from datetime import datetime

from fastapi import APIRouter, FastAPI, status

from src.domain import Record

main = APIRouter()


def create_app() -> FastAPI:
    """Factory function."""
    app = FastAPI()
    app.include_router(
        main,
        responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
    )
    app.mount('/', main)
    return app


@main.get('/', status_code=200)
def read_root() -> dict:
    """Test route."""
    return {'message': 'Hello Template'}


@main.post('/record', status_code=201)
def create_record(record_data: Record) -> dict:
    """Create record."""
    return record_data


@main.put('/record', status_code=200)
def update_record(record_data: Record) -> dict:
    """Update record."""
    return record_data


@main.get('/records', status_code=200)
def get_record() -> list[dict]:
    """Get records to current month."""
    now = datetime.now()
    date_time = now.strftime('%m/%d/%Y')
    record_data = []
    record_data.append(
        Record(
            id_=1,
            user_id=1,
            account_id=1,
            category_id=1,
            type_='debit',
            amount=10.0,
            date=date_time,
            description='one description',
        )
    )
    record_data.append(
        Record(
            id_=2,
            user_id=1,
            account_id=1,
            category_id=1,
            type_='debit',
            amount=20.0,
            date=date_time,
            description='second description',
        )
    )

    return record_data
