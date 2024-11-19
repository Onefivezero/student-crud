from src.app.models.student import StudentCreationData, StudentResponse
from src.internal.model.student import Student
from src.internal.persistence.student import StudentPersistence


class StudentService:

    @classmethod
    def get_customer(cls, id_: int) -> StudentResponse:
        student: Student = StudentPersistence.get_student(id_=id_)
        return StudentResponse(
            id=student.id,
            name=student.name,
            surname=student.surname
        )

    @classmethod
    def list_customers(cls) -> list[StudentResponse]:
        students: list[Student] = StudentPersistence.list_students()
        print(students)
        return [
            StudentResponse(
                id=student.id,
                name=student.name,
                surname=student.surname
            )
            for student in students
        ]

    @classmethod
    def create_customer(cls, student_data: StudentCreationData) -> StudentResponse:
        student: Student = StudentPersistence.create_student(
            name=student_data.name,
            surname=student_data.surname,
        )
        return StudentResponse(
            id=student.id,
            name=student.name,
            surname=student.surname
        )
