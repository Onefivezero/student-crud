from starlette import status
from src.internal.model.student import Student


class TestCreateStudentAPI:
    def test_create_student_api(self, client, db_session):
        student_data = {
            "name": "John",
            "surname": "Doe",
        }

        response = client.post(url="/students", json=student_data)

        assert response.status_code == status.HTTP_200_OK

        response_dict = response.json()

        expected_student_data = {
            **student_data,
            "id": response_dict["id"]
        }

        assert expected_student_data == response_dict

        db_result = db_session.get(Student, response_dict["id"])

        assert {
            "id": db_result.id,
            "name": db_result.name,
            "surname": db_result.surname
        } == response_dict