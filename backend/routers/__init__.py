from fastapi import APIRouter
from .base import router as base_router

routers = APIRouter(prefix="/api")
routers.include_router(base_router, prefix="/base")
