from starlette import status
from src.internal.model.classes import Class


class TestListClassesAPI:

    def test_list_all_classs_returns_correct_data(self, client, db_session):
        s1 = Class(name="Software - 101", teacher_name="Teacher McTeacher", description="1")
        s2 = Class(name="Software - 102", teacher_name="Teacher McTeacher", description="2")
        db_session.add_all([s1, s2])
        db_session.flush()

        response = client.get("/classes")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data == [
            {"id": s1.id, "name": "Software - 101", "teacher_name": "Teacher McTeacher", "description": "1"},
            {"id": s2.id, "name": "Software - 102", "teacher_name": "Teacher McTeacher", "description": "2"},
        ]

    def test_list_classs_returns_empty_when_no_records(self, client):
        response = client.get("/classes")

        assert response.status_code == 200
        assert response.json() == []