from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASS = "password"
DB_NAME = "postgres"


DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine: AsyncEngine = create_async_engine(url=DATABASE_URL)

async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False  # сессии чтобы не истекали после окммита
)
print(type(async_session_maker))

# Base is Used for migrations
class Base(DeclarativeBase):
    ...
