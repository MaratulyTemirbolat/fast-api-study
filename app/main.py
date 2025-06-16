# Python
from typing import Optional
from datetime import date

# FastAPI
from fastapi import FastAPI, Query


app: FastAPI = FastAPI()


@app.get(path="/hotels")
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(default=None, ge=1, le=5)
):
    """Handle GET-request to return all the hotels."""
    return "All the hotels"
