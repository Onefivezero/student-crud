from pydantic import BaseModel


class ClassResponse(BaseModel):
    id: int
    name: str
    teacher_name: str
    description: str | None = None


class ClassCreationData(BaseModel):
    name: str
    teacher_name: str
    description: str | None = None
