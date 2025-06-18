# Python modules
from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
)

# Project modules
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
