from fastapi import APIRouter, FastAPI

from .faststream import queue_router

app = FastAPI()

api_router = APIRouter()
app.include_router(queue_router)
app.include_router(api_router)
