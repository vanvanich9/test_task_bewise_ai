from .models import Question
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.schemas.question import QuestionResponse

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from backend.config import POSTGRES_URI


def get_session(coroutine):
    async def wrapper(*args, **kwargs):
        engine = create_async_engine(POSTGRES_URI, echo=True)
        async_session = async_sessionmaker(engine, expire_on_commit=False)
        async with async_session() as session:
            result = await coroutine(session, *args, **kwargs)
        await engine.dispose()
        return result

    return wrapper


@get_session
async def get_question(session: AsyncSession, question_id: int):
    stmt = select(Question).where(Question.id == question_id)
    result = await session.execute(stmt)
    return result.first()


@get_session
async def add_all_questions(session: AsyncSession, questions: list[QuestionResponse]):
    questions_db = list()
    for question in questions:
        questions_db.append(Question(**question.model_dump()))

    session.add_all(questions_db)
    await session.commit()
    return questions_db
