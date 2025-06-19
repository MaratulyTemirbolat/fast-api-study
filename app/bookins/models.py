# Python modules
from datetime import date
from sqlalchemy import (
    ForeignKey,
    Date,
    Computed,
)
from sqlalchemy.orm import mapped_column, Mapped

# Project modules
from app.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(
        ForeignKey(
            "rooms.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )
    date_from: Mapped[date] = mapped_column(Date, nullable=False)
    date_to: Mapped[date] = mapped_column(Date, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    total_cost: Mapped[int] = mapped_column(
        Computed(sqltext="(date_to - date_from) * price")
    )
    total_days: Mapped[int] = mapped_column(
        Computed(sqltext="date_to - date_from")
    )
