from fastapi.exceptions import ValidationException
from fastapi import FastAPI
from middleware import limit_request
from middleware import validation_exception_handler

from routers import rating_router, genre_router, director_router, description_router, film_router, auth_router

app = FastAPI()

app.middleware("http")(limit_request)
app.add_exception_handler(ValidationException, validation_exception_handler)

app.include_router(genre_router, tags=["genres"])
app.include_router(director_router, tags=["directors"])
app.include_router(description_router, tags=["descriptions"])
app.include_router(film_router, tags=["films"])
app.include_router(rating_router, tags=["rating"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
