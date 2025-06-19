# Python
from sqlalchemy import select, Result
from sqlalchemy.sql.selectable import Select

# FastAPI
from fastapi import APIRouter

# Project
from app.database import async_session_maker
from app.bookins.models import Booking
from app.bookins.dao import BookingDAO


router: APIRouter = APIRouter(
    prefix="/bookings",
    tags=["Bookings V1 related endpoints"]
)


@router.get("")
async def get_bookings():
    async with async_session_maker() as async_session:
        # query: Select[tuple[Booking]] = select(Booking)  # SELECT * FROM bookings;
        # query_result: Result[tuple[Booking]] = await async_session.execute(query)
        # # 1 - All
        # # query_result.all() - Return [(Booking #1, ), (Booking #2,), ...]
        # # 2 - Mapping all
        # # query_result.mappings().all() - Return [{"Booking": <Booking #1>}, {"Booking": <Booking #2>}, ...]
        # # Если перед query_result.mappings().all() сделать еще select(Booking.__table__.columns),
        # # то есть взять не всю модель целиком, а только колонки и тогда вернется потом список кортежей всех полей
        # bookings: list[Booking] = query_result.scalars().all()  # Return [Booking #1, Booking #2, ...]
        # return bookings
        bookings: list[Booking] = await BookingDAO.get_all_by_scalar()
        return bookings
        

