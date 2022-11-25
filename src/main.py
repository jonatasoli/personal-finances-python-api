from fastapi import APIRouter, FastAPI

main = APIRouter()

def create_app():
    app = FastAPI()
    app.mount("/", main)
    return app


@main.get('/', status_code=200)
def read_root():
    return dict(message='Hello Template')
