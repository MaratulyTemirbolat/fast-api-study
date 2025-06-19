# Python modules
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

# Project modules
from app.database import Base


class User(Base):
    EMAIL_MAX_LEN = 50

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(length=EMAIL_MAX_LEN),
        nullable=False,
    )
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"<User #{self.email}>"
