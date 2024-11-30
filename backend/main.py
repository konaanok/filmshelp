from collections import defaultdict
from time import time
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse
from fastapi import FastAPI

from routers.genre_routers import genre_router
from routers.director_routers import director_router
from routers.description_routers import description_router
from routers.film_routers import film_router
from routers.user_router import auth_router

app = FastAPI()

request_counter = defaultdict(list)
limit = 5
time_lim = 1

@app.middleware("http")
async def limit_request(request: Request, call_next):
    user_ip = request.client.host 
    current_time = time()
    request_counter[user_ip] = [
        timestamp for timestamp in request_counter[user_ip]
        if timestamp > current_time - time_lim
    ]
    if len(request_counter[user_ip]) >= limit:
        return JSONResponse(
            content="Too Many Requests. Please try again later.",
            status_code=429
)
    request_counter[user_ip].append(current_time)
    return await call_next(request)



@app.exception_handler(ValidationException)
async def validation_exception_handler(request:Request, exc: ValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )

app.include_router(genre_router, tags=["genres"])
app.include_router(director_router, tags=["directors"])
app.include_router(description_router, tags=["descriptions"])
app.include_router(film_router, tags=["films"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(rating_router, tags=["rating"])
