from starlette import status
from starlette.testclient import TestClient

from src.app.app import app
from src.internal.model.student import Student
from test.app.student import TestBase


class TestCreateStudentAPI(TestBase):
    client = TestClient(app=app)

    def test__create_student_api(self):
        student = {
            "name": "John",
            "surname": "Doe",
        }

        response = self.client.post(url="/students", json=student)
        self.assertEqual(status.HTTP_200_OK, response.status_code, response.content)

        response_dict = response.json()
        self.assertEqual({
            "id": response_dict["id"],
            "name": student["name"],
            "surname": student["surname"],
        }, response.json())

        db_result = self.session.get(Student, response_dict["id"])
        self.assertEqual(response_dict["id"], db_result.id)
        self.assertEqual(response_dict["name"], db_result.name)
        self.assertEqual(response_dict["surname"], db_result.surname)
