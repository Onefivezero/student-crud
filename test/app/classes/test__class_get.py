from starlette import status
from src.internal.model.classes import Class


class TestGetClassAPI:
    def test_get_class_success(self, client, db_session):
        name = "Software - 101"
        teacher_name = "Teacher McTeacher"
        description = "lorem ipsum"
        new_class = Class(name=name, teacher_name=teacher_name, description=description)
        
        db_session.add(new_class)
        db_session.flush()
        
        class_id = new_class.id

        response = client.get(url=f"/classes/{class_id}")

        assert response.status_code == status.HTTP_200_OK
        
        response_dict = response.json()
        assert response_dict == {
            "id": class_id,
            "name": name,
            "teacher_name": teacher_name,
            "description": description,
        }

    def test_get_class_not_found(self, client):
        response = client.get(url="/classes/9999")
        
        assert response.status_code == status.HTTP_404_NOT_FOUND