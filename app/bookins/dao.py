# DAO - Data Access Object
# Project modules
from app.bookins.models import Booking
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO[Booking]):

    model = Booking

