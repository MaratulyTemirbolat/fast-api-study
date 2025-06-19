# Python
from typing import Optional
from datetime import date
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Query, Depends

# Project
from app.bookins.router import router as bookings_router

app: FastAPI = FastAPI()

app.include_router(router=bookings_router)


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


class HotelSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(default=None, ge=1, le=5)
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars

@app.get(path="/hotels")
def get_hotels(search_args: HotelSearchArgs = Depends()) -> list[SHotel]:
    """Handle GET-request to return all the hotels."""
    hotels = [
        {
            "address": "Address 1",
            "name": "Super Hotel 1",
            "stars": 5
        }
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post(path="/bookings")
def add_booking(booking: SBooking):
    ...
