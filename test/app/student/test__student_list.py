from starlette import status
from starlette.testclient import TestClient

from src.app.app import app
from src.internal.model.student import Student
from src.internal.persistence.student import StudentPersistence
from test.app.student import TestBase


class TestListStudentsAPI(TestBase):
    client = TestClient(app=app)

    def test__create_student_api(self):
        full_names = (
            ("John", "Doe"),
            ("Jane", "Smith"),
            ("Matt", "Baker"),
        )
        students = []
        for name, surname in full_names:
            student = StudentPersistence.create_student(name=name, surname=surname)
            students.append(student)

        response = self.client.get(url="/students")
        self.assertEqual(status.HTTP_200_OK, response.status_code, response.content)

        response_dict = response.json()
        self.assertCountEqual(
            [
                {
                    "id": student.id,
                    "name": student.name,
                    "surname": student.surname,
                }
                for student in students
            ],
            response_dict
        )
