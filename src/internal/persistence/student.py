from sqlalchemy import select

from src.internal.model.student import Student
from src.internal.persistence import create_session, engine
from src.internal.util.id_generator import IDGenerator


class StudentPersistence:

    @classmethod
    def get_student(cls, id_: int) -> Student:
        session = create_session()
        with session:
            statement = select(Student).where(Student.id == id_)
            result = session.execute(statement).one()

        return result[0]

    @classmethod
    def list_students(cls) -> list[Student]:
        session = create_session()
        with session:
            statement = select(Student)
            result = session.execute(statement)
            return [res[0] for res in result]

    @classmethod
    def create_student(
        cls,
        name: str,
        surname: str
    ) -> Student:
        student = Student(
            id=IDGenerator.generate_unique_id(),
            name=name,
            surname=surname,
        )

        session = create_session()
        with session:
            session.add(student)
            session.commit()

        return student
