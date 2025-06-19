# DAO - Data Access Object

# Python modules
from typing import (
    Any,
    Sequence,
    TypeVar,
    Type,
    Generic,
    Optional,
)
from sqlalchemy import select, Select
from sqlalchemy.engine import Result

# Project modules
from app.database import async_session_maker, Base


T = TypeVar(name="T", bound=Base)

class BaseDAO(Generic[T]):
    model: Type[T]

    @classmethod
    async def get_by_id_or_none(cls, model_id: int) -> Optional[T]:
        return await cls.get_one_or_none(id=model_id)

    @classmethod
    async def get_one_or_none(cls, **filters: dict[str, Any]) -> Optional[T]:
        async with async_session_maker() as assync_session:
            query: Select[T] = select(cls.model).filter_by(**filters)
            query_result: Result[T] = await assync_session.execute(query)
            object: Optional[T] = query_result.scalar_one_or_none()
            return object

    @classmethod
    async def get_all_by_scalar(cls, **filters: dict[str, Any]) -> Sequence[T]:

        async with async_session_maker() as assync_session:
            query: Select[T] = select(cls.model).filter_by(**filters)
            query_result: Result[T] = await assync_session.execute(query)
            results: list[T] = query_result.scalars().all()
            return results
