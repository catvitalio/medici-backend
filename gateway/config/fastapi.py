from fastapi import APIRouter, FastAPI

from api.auth import router as auth_router
from api.user import router as register_router

app = FastAPI()

router = APIRouter(prefix='/api')
router.include_router(auth_router)
router.include_router(register_router)

app.include_router(router)
