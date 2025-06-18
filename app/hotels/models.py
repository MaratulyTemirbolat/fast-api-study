# Python modules
from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    ForeignKey,
)

# Project modules
from app.database import Base


class Hotels(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON, nullable=True)
    room_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)


class Room(Base):
    __tablename__ = "rooms"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    hotel_id = Column(
        ForeignKey(column="hotels.id"),
        nullable=False,
    )
    name = Column(
        String,
        nullable=False,
    )
    description = Column(
        String,
        nullable=True,
    )
    price = Column(
        Integer,
        nullable=False
    )
    services = Column(JSON, nullable=True)
    quantity = Column(
        Integer,
        nullable=False
    )
    image_id = Column(Integer)
