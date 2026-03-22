from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src.app.models.student import StudentCreationData, StudentResponse
from src.internal.model.student import Student
from src.internal.persistence.student import StudentPersistence


class StudentService:

    @classmethod
    def get_student(cls, db: Session, id_: int) -> StudentResponse:
        student: Student = StudentPersistence.get_student(db=db, id_=id_)

        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Student with id={id_} not found."
            )

        return StudentResponse(
            id=student.id,
            name=student.name,
            surname=student.surname
        )

    @classmethod
    def list_students(cls, db: Session) -> list[StudentResponse]:
        students: list[Student] = StudentPersistence.list_students(db=db)
        return [
            StudentResponse(
                id=student.id,
                name=student.name,
                surname=student.surname
            )
            for student in students
        ]

    @classmethod
    def create_student(cls, db: Session, student_data: StudentCreationData) -> StudentResponse:
        student: Student = StudentPersistence.create_student(
            db=db,
            name=student_data.name,
            surname=student_data.surname,
        )

        db.commit()
        db.refresh(student)

        return StudentResponse(
            id=student.id,
            name=student.name,
            surname=student.surname
        )
