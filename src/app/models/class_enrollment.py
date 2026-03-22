from pydantic import BaseModel


class ClassEnrollmentCreationData(BaseModel):
    student_id: int | None = None
    class_id: int | None = None


class ClassEnrollmentResponse(BaseModel):
    student_id: int
    class_id: int
