import datetime

from pydantic import BaseModel


class QuestionResponse(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


class QuestionsNumberRequest(BaseModel):
    questions_num: int
