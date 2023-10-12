from fastapi import APIRouter

from .base import router as base_router
from .question import router as question_router

routers = APIRouter(prefix="/api")
routers.include_router(base_router, prefix="/base")
routers.include_router(question_router, prefix="/questions")
