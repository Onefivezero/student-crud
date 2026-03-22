from datetime import datetime, timezone

from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from src.internal.model.base import Base


class ClassEnrollment(Base):
    __tablename__ = "enrollment"

    student_id: Mapped[int] = mapped_column(ForeignKey("student.id"), primary_key=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("class.id"), primary_key=True)

    enrolled_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    final_grade: Mapped[str] = mapped_column(nullable=True)

    # relations
    student: Mapped["Student"] = relationship(back_populates="class_enrollments")
    class_: Mapped["Class"] = relationship(back_populates="class_enrollments")