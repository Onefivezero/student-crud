from starlette import status
from src.internal.model.classes import Class


class TestCreateClassAPI:
    def test_create_class_api(self, client, db_session):
        class_data = {
            "name": "Software 101",
            "teacher_name": "Teacher McTeacher",
            "description": "lorem ipsum",
        }

        response = client.post(url="/classes", json=class_data)

        assert response.status_code == status.HTTP_200_OK

        response_dict = response.json()

        expected_class_data = {
            **class_data,
            "id": response_dict["id"]
        }

        assert expected_class_data == response_dict

        db_result = db_session.get(Class, response_dict["id"])

        assert {
            "id": db_result.id,
            "name": db_result.name,
            "teacher_name": db_result.teacher_name,
            "description": db_result.description,
        } == response_dict