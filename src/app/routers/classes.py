import fastapi
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.app.models.classes import ClassResponse, ClassCreationData
from src.app.services.classes import ClassService
from src.internal.persistence import get_db

class_router = fastapi.APIRouter()


@class_router.get("/classes")
async def list_classes(db: Session = Depends(get_db)) -> list[ClassResponse]:
    return ClassService.list_classes(db)


@class_router.get("/classes/{id_}")
async def get_class(id_: int, db: Session = Depends(get_db)) -> ClassResponse:
    return ClassService.get_class(db, id_=id_)


@class_router.post("/classes")
async def create_class(class_data: ClassCreationData, db: Session = Depends(get_db)) -> ClassResponse:
    return ClassService.create_class(db, class_data=class_data)

