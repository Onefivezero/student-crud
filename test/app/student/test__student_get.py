from starlette import status
from starlette.testclient import TestClient

from src.app.app import app
from src.internal.model.student import Student
from src.internal.persistence.student import StudentPersistence
from test.app.student import TestBase


class TestGetStudentAPI(TestBase):
    client = TestClient(app=app)

    def test__create_student_api(self):
        name="John"
        surname="Doe"

        student = StudentPersistence.create_student(name=name, surname=surname)
        self.assertEqual(name, student.name)
        self.assertEqual(surname, student.surname)

        response = self.client.get(url=f"/students/{student.id}")
        self.assertEqual(status.HTTP_200_OK, response.status_code, response.content)

        response_dict = response.json()
        self.assertEqual({
            "id": student.id,
            "name": name,
            "surname": surname,
        }, response_dict)
