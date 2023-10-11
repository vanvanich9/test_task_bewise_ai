from .base import SessionLocal
from .models import Question
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.schemas.question import QuestionRequest


def get_session(coroutine):
    async def wrapper(*args, **kwargs):
        return await coroutine(SessionLocal, *args, **kwargs)

    return wrapper


@get_session
async def get_question(session: AsyncSession, question_id: int):
    stmt = select(Question).where(Question.id == question_id)
    result = await session.execute(stmt)
    return result


@get_session
async def add_question(session: AsyncSession, question: QuestionRequest):
    question_db = Question(**question.model_dump())
    session.add(question_db)
    return question_db
