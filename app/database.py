# Python
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import DeclarativeBase

# Project modules
from app.config import settings


engine: AsyncEngine = create_async_engine(url=settings.database_dsn_psycopg2)

async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False  # сессии чтобы не истекали после окммита
)

# Base is Used for migrations
class Base(DeclarativeBase):
    ...
