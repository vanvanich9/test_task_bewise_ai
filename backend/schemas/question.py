from pydantic import BaseModel
import datetime


class QuestionResponse(BaseModel):
    id: int | None = None
    question: str | None = None
    answer: str | None = None
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

    class Config:
        from_attributes = True


class QuestionsNumberRequest(BaseModel):
    questions_num: int
