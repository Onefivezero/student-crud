from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.internal.model.base import Base


class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(30))

    def __str__(self) -> str:
        return f"Student(id={self.id!r}, name={self.name!r}, surname={self.surname!r})"
