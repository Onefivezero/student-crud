from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.internal.model.base import Base


class Class(Base):
    __tablename__ = "class"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    teacher_name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)

    def __str__(self) -> str:
        return (
            f"Class(id={self.id}, name={self.name}, teacher_name={self.teacher_name}, description={self.description})"
        )