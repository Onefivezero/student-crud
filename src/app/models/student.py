from pydantic import BaseModel


class StudentResponse(BaseModel):
    id: int
    name: str
    surname: str


class StudentCreationData(BaseModel):
    name: str
    surname: str
