# Python modules
from typing import Optional
from sqlalchemy import (
    String,
    JSON,
    ForeignKey,
    VARCHAR,
    Text,
)
from sqlalchemy.orm import mapped_column, Mapped

# Project modules
from app.database import Base


class Hotel(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=50), nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    services: Mapped[list[str]] = mapped_column(JSON, nullable=True)
    room_quantity: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int]

    def __repr__(self) -> str:
        return f"<Hotel #{self.name}>"


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    hotel_id: Mapped[int] = mapped_column(
        ForeignKey(
            "hotels.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(
        VARCHAR(length=50),
        nullable=False,
    )
    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    price: Mapped[int] = mapped_column(
        nullable=False
    )
    services: Mapped[list[str]] = mapped_column(JSON, nullable=True)
    quantity: Mapped[int] = mapped_column(
        nullable=False
    )
    image_id: Mapped[int]

    def __repr__(self) -> str:
        return f"<Room #{self.name}>"