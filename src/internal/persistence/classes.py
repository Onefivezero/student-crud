from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from src.internal.model.classes import Class


class ClassPersistence:

    @classmethod
    def get_class(cls, db: Session, id_: int) -> Class | None:
        statement = select(Class).where(Class.id == id_)
        result = db.execute(statement).one_or_none()

        return result[0] if result else None

    @classmethod
    def list_classes(cls, db: Session) -> Sequence[Class]:
        statement = select(Class)
        result = db.execute(statement)
        return result.scalars().all()

    @classmethod
    def create_class(
        cls,
        db: Session,
        name: str,
        teacher_name: str,
        description: str | None = None,
    ) -> Class:
        new_class = Class(name=name, teacher_name=teacher_name, description=description)
        db.add(new_class)
        db.flush()
        return new_class
