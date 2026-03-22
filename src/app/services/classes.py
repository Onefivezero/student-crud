from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src.app.models.classes import ClassCreationData, ClassResponse
from src.internal.model.classes import Class
from src.internal.persistence.classes import ClassPersistence


class ClassService:

    @classmethod
    def get_class(cls, db: Session, id_: int) -> ClassResponse:
        class_: Class = ClassPersistence.get_class(db=db, id_=id_)

        if not class_:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Class with id={id_} not found."
            )

        return ClassResponse(
            id=class_.id,
            name=class_.name,
            teacher_name=class_.teacher_name,
            description=class_.description,
        )

    @classmethod
    def list_classes(cls, db: Session) -> list[ClassResponse]:
        classes: list[Class] = ClassPersistence.list_classes(db=db)
        return [
            ClassResponse(
                id=class_.id,
                name=class_.name,
                teacher_name=class_.teacher_name,
                description=class_.description,
            )
            for class_ in classes
        ]

    @classmethod
    def create_class(cls, db: Session, class_data: ClassCreationData) -> ClassResponse:
        class_: Class = ClassPersistence.create_class(
            db=db,
            name=class_data.name,
            teacher_name=class_data.teacher_name,
            description=class_data.description,
        )

        db.commit()
        db.refresh(class_)

        return ClassResponse(
            id=class_.id,
            name=class_.name,
            teacher_name=class_.teacher_name,
            description=class_data.description,
        )
