"""Main module."""

from fastapi import APIRouter, FastAPI

main = APIRouter()


def create_app() -> FastAPI:
    """Factory function."""
    app = FastAPI()
    app.mount('/', main)
    return app


@main.get('/', status_code=200)
def read_root() -> dict:
    """Test route."""
    return {'message': 'Hello Template'}
