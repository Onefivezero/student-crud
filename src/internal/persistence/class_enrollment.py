from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from src.internal.model.class_enrollment import ClassEnrollment


class ClassEnrollmentPersistence:

    @classmethod
    def get_class_enrollment(
        cls,
        db: Session,
        student_id: int,
        class_id: int,
    ) -> ClassEnrollment | None:
        statement = select(ClassEnrollment).where(
            ClassEnrollment.class_id == class_id,
            ClassEnrollment.student_id == student_id,
        )
        result = db.execute(statement).one_or_none()
        return result[0] if result else None

    @classmethod
    def create_class_enrollment(
        cls,
        db: Session,
        student_id: int,
        class_id: int,
    ) -> ClassEnrollment:
        enrollment = ClassEnrollment(student_id=student_id, class_id=class_id)
        db.add(enrollment)
        db.flush()
        return enrollment

    @classmethod
    def list_class_enrollments(
        cls,
        db: Session,
        student_id: int | None = None,
        class_id: int | None = None,
    ) -> Sequence[ClassEnrollment]:
        stmt = select(ClassEnrollment)

        if student_id is not None:
            stmt = stmt.where(ClassEnrollment.student_id == student_id)
        if class_id is not None:
            stmt = stmt.where(ClassEnrollment.class_id == class_id)

        return db.execute(stmt).scalars().all()