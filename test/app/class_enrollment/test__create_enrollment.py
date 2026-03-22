import pytest
from starlette import status
from src.internal.model import Class, Student
from src.internal.model.class_enrollment import ClassEnrollment


class TestCreateEnrollmentAPI:

    @pytest.fixture(autouse=True)
    def setup_data(self, db_session):
        """Prepare a student and a class to link together."""
        self.student = Student(name="Charlie", surname="Brown")
        self.classroom = Class(name="CS50", teacher_name="David Malan")

        db_session.add_all([self.student, self.classroom])
        db_session.flush()
        self.s_id = self.student.id
        self.c_id = self.classroom.id
        db_session.commit()

    def test_create_enrollment_success(self, client, db_session):
        payload = {
            "student_id": self.s_id,
            "class_id": self.c_id
        }

        response = client.post("/class-enrollments/", json=payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.content == b""

        db_enrollment = db_session.query(ClassEnrollment).filter_by(
            student_id=self.s_id,
            class_id=self.c_id
        ).first()

        assert db_enrollment is not None
        assert db_enrollment.student_id == self.s_id

    def test_create_duplicate_enrollment_fails(self, client, db_session):
        payload = {"student_id": self.s_id, "class_id": self.c_id}

        client.post("/class-enrollments/", json=payload)
        response = client.post("/class-enrollments/", json=payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["detail"] == "Student is already enrolled in this class."

    def test_create_enrollment_invalid_ids(self, client):
        payload = {"student_id": 9999, "class_id": 8888}

        response = client.post("/class-enrollments/", json=payload)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "not found" in response.json()["detail"].lower()