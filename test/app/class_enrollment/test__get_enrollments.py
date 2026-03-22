import pytest

from src.internal.model import Class, Student
from src.internal.model.class_enrollment import ClassEnrollment


class TestGetClassEnrollments:
    
    @pytest.fixture(autouse=True)
    def setup_data(self, db_session):
        self.s1 = Student(name="Alice", surname="Smith")
        self.s2 = Student(name="Bob", surname="Jones")
        self.c1 = Class(name="Math 101", teacher_name="Teacher McTeacher")
        self.c2 = Class(name="History 202", teacher_name="Teacher McTeacher Jr.")
        
        db_session.add_all([self.s1, self.s2, self.c1, self.c2])
        db_session.flush()

        self.e1 = ClassEnrollment(student_id=self.s1.id, class_id=self.c1.id)
        self.e2 = ClassEnrollment(student_id=self.s1.id, class_id=self.c2.id)
        self.e3 = ClassEnrollment(student_id=self.s2.id, class_id=self.c1.id)
        
        db_session.add_all([self.e1, self.e2, self.e3])
        db_session.commit()

    def test_filter_by_student(self, client):
        response = client.get(f"/class-enrollments/?student_id={self.s1.id}")
        data = response.json()

        assert response.status_code == 200

        expected = [
            {"student_id": self.s1.id, "class_id": self.c1.id},
            {"student_id": self.s1.id, "class_id": self.c2.id}
        ]
        assert sorted(data, key=lambda x: x["class_id"]) == sorted(expected, key=lambda x: x["class_id"])

    def test_filter_by_class(self, client):
        response = client.get(f"/class-enrollments/?class_id={self.c1.id}")
        data = response.json()

        assert response.status_code == 200

        expected = [
            {"student_id": self.s1.id, "class_id": self.c1.id},
            {"student_id": self.s2.id, "class_id": self.c1.id}
        ]
        assert sorted(data, key=lambda x: x["student_id"]) == sorted(expected, key=lambda x: x["student_id"])

    def test_filter_by_both(self, client):
        url = f"/class-enrollments/?student_id={self.s1.id}&class_id={self.c2.id}"
        response = client.get(url)
        data = response.json()

        assert response.status_code == 200
        assert data == [{"student_id": self.s1.id, "class_id": self.c2.id}]

    def test_filter_no_results(self, client):
        response = client.get(f"/class-enrollments/?student_id={self.s2.id}&class_id={self.c2.id}")
        
        assert response.status_code == 200
        assert response.json() == []