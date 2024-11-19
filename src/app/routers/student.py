import fastapi

from src.app.models.student import StudentResponse, StudentCreationData
from src.app.services.student import StudentService

student_router = fastapi.APIRouter()


@student_router.get("/students")
async def list_students() -> list[StudentResponse]:
    return StudentService.list_customers()


@student_router.get("/students/{id_}")
async def get_student(id_: int) -> StudentResponse:
    return StudentService.get_customer(id_=id_)


@student_router.post("/students")
async def create_student(student_data: StudentCreationData) -> StudentResponse:
    return StudentService.create_customer(student_data=student_data)
