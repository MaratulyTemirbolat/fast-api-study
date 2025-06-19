# Python modules
from pydantic import BaseModel, ConfigDict
from datetime import date


class SBookingBase(BaseModel):
    id:  int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    # class Config:
    #     orm_mode = True  # orm_mode поменял название во 2 версии Pydantic
    model_config = ConfigDict(from_attributes=True)
