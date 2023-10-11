from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from backend.config import POSTGRES_URI

SQLALCHEMY_DATABASE_URL = POSTGRES_URI

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
