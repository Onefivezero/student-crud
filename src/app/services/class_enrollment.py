from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src.app.models.class_enrollment import ClassEnrollmentResponse, ClassEnrollmentCreationData
from src.internal.persistence.class_enrollment import ClassEnrollmentPersistence
from src.internal.persistence.classes import ClassPersistence
from src.internal.persistence.student import StudentPersistence


class ClassEnrollmentAPIService:

    @classmethod
    def enroll_student_in_class(cls, request_data: ClassEnrollmentCreationData, db: Session) -> None:
        student_id, class_id = request_data.student_id, request_data.class_id

        student = StudentPersistence.get_student(id_=student_id, db=db)
        class_ = ClassPersistence.get_class(id_=class_id, db=db)

        if not student or not class_:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student or Class not found."
            )

        if ClassEnrollmentPersistence.get_class_enrollment(student_id=student_id, class_id=class_id, db=db):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Student is already enrolled in this class."
            )

        ClassEnrollmentPersistence.create_class_enrollment(
            db=db, student_id=student_id, class_id=class_id
        )
        db.commit()

    @classmethod
    def get_filtered_enrollments(
        cls,
        db: Session,
        student_id: int | None = None,
        class_id: int | None = None
    ) -> list[ClassEnrollmentResponse]:
        enrollments = ClassEnrollmentPersistence.list_class_enrollments(
            db=db,
            student_id=student_id,
            class_id=class_id
        )

        return [
            ClassEnrollmentResponse(
                student_id=enrollment.student_id,
                class_id=enrollment.class_id,
            )
            for enrollment in enrollments
        ]