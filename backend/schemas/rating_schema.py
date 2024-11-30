from pydantic import BaseModel
from typing import Optional

class MessageCreateRating(BaseModel):
    message: str

class MessageRatingResponse(BaseModel):
    message: str

class FilmRating(BaseModel):
    rating_web: float
    rating_average: float

    class Config:
        orm_mode = True

class RatingResponse(BaseModel):
    username: str
    rating_user: float
    review: Optional[str] = None

    class Config:
        orm_mode = True

class RatingCreate(BaseModel):
    film_title: str
    username: str
    rating_user: float
    review: Optional[str] = None