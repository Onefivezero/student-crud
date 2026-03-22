from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from src.internal.model.student import Student


class StudentPersistence:

    @classmethod
    def get_student(cls, db: Session, id_: int) -> Student | None:
        statement = select(Student).where(Student.id == id_)
        result = db.execute(statement).one_or_none()

        return result[0] if result else None

    @classmethod
    def list_students(cls, db: Session) -> Sequence[Student]:
        statement = select(Student)
        result = db.execute(statement)
        return result.scalars().all()

    @classmethod
    def create_student(
        cls,
        db: Session,
        name: str,
        surname: str
    ) -> Student:
        new_student = Student(name=name, surname=surname)
        db.add(new_student)
        db.flush()
        return new_student
