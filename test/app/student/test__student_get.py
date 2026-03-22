from starlette import status
from src.internal.model.student import Student


class TestGetStudentAPI:
    def test_get_student_success(self, client, db_session):
        name = "John"
        surname = "Doe"
        new_student = Student(name=name, surname=surname)
        
        db_session.add(new_student)
        db_session.flush()
        
        student_id = new_student.id

        response = client.get(url=f"/students/{student_id}")

        assert response.status_code == status.HTTP_200_OK
        
        response_dict = response.json()
        assert response_dict == {
            "id": student_id,
            "name": name,
            "surname": surname,
        }

    def test_get_student_not_found(self, client):
        response = client.get(url="/students/9999")
        
        assert response.status_code == status.HTTP_404_NOT_FOUND