import datetime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_text: Mapped[str]
    answer: Mapped[str]
    created_at: Mapped[datetime.datetime]
    updated_at: Mapped[datetime.datetime]
