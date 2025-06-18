# Python modules
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Date,
    Computed,
)

# Project modules
from app.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey(column="rooms.id"))
    user_id = Column(ForeignKey(column="users.id"))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed(sqltext="(date_to - date_from) * price"))
    total_days = Column(Integer, Computed(sqltext="date_to - date_from"))
