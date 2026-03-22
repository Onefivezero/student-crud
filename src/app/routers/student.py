import fastapi
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.app.models.student import StudentResponse, StudentCreationData
from src.app.services.student import StudentService
from src.internal.persistence import get_db

student_router = fastapi.APIRouter()


@student_router.get("/students")
async def list_students(db: Session = Depends(get_db)) -> list[StudentResponse]:
    return StudentService.list_students(db)


@student_router.get("/students/{id_}")
async def get_student(id_: int, db: Session = Depends(get_db)) -> StudentResponse:
    return StudentService.get_student(db, id_=id_)


@student_router.post("/students")
async def create_student(student_data: StudentCreationData, db: Session = Depends(get_db)) -> StudentResponse:
    return StudentService.create_student(db, student_data=student_data)

