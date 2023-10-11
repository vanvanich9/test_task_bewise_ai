from pydantic import BaseModel


class HealthResponse(BaseModel):
    version: str
    message: str
