from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.app.models.class_enrollment import ClassEnrollmentResponse, ClassEnrollmentCreationData
from src.app.services.class_enrollment import ClassEnrollmentAPIService
from src.internal.persistence import get_db

class_enrollment_router = APIRouter (prefix="/class-enrollments")


@class_enrollment_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_class=Response,
)
def create_class_enrollment(request_data: ClassEnrollmentCreationData, db: Session = Depends(get_db)) -> None:
    ClassEnrollmentAPIService.enroll_student_in_class(request_data=request_data, db=db)


@class_enrollment_router.get("/")
def list_enrollments(
    student_id: int | None = None,
    class_id: int | None = None,
    db: Session = Depends(get_db)
) -> list[ClassEnrollmentResponse]:
    return ClassEnrollmentAPIService.get_filtered_enrollments(
        student_id=student_id,
        class_id=class_id,
        db=db,
    )