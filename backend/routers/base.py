from fastapi import APIRouter

from backend import version
from backend.schemas.base import HealthResponse

router = APIRouter()


@router.get("/health")
async def health() -> HealthResponse:
    return HealthResponse(version=version or "0.0.0", message="App work")
