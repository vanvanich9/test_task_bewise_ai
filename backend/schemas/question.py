from pydantic import BaseModel
import datetime


class QuestionRequest(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
