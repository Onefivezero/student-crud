from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from src.internal.model.base import Base


class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    surname: Mapped[str] = mapped_column(String(30), nullable=False)

    # relations
    class_enrollments: Mapped[list["ClassEnrollment"]] = relationship(back_populates="student")

    def __str__(self) -> str:
        return f"Student(id={self.id}, name={self.name}, surname={self.surname})"
