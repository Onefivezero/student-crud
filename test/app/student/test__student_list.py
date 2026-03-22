from starlette import status
from src.internal.model.student import Student


class TestListStudentsAPI:

    def test_list_all_students_returns_correct_data(self, client, db_session):
        s1 = Student(name="John", surname="Doe")
        s2 = Student(name="Jane", surname="Smith")
        db_session.add_all([s1, s2])
        db_session.flush()

        response = client.get("/students")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data == [
            {"id": s1.id, "name": "John", "surname": "Doe"},
            {"id": s2.id, "name": "Jane", "surname": "Smith"},
        ]

    def test_list_students_returns_empty_when_no_records(self, client):
        response = client.get("/students")

        assert response.status_code == 200
        assert response.json() == []