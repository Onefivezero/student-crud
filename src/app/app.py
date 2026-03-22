from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from src.app.routers.class_enrollment import class_enrollment_router
from src.app.routers.classes import class_router
from src.app.routers.student import student_router

app = FastAPI()

app.include_router(student_router)
app.include_router(class_router)
app.include_router(class_enrollment_router)

@app.exception_handler(500)
async def internal_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=jsonable_encoder({"code": 500, "msg": "Internal Server Error"})
    )
