from typing import Dict, List, Union
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_film_db
from repositories.film_repository import FilmRepository
from repositories.rating_average_repository import RatingAverageRepository
from repositories.rating_repository import RatingRepository
from repositories.user_repository import UserRepository
from schemas.rating_schema import FilmRating, MessageCreateRating, RatingCreate, RatingResponse
from services.rating_average_service import RatingAverageService
from services.rating_service import RatingService

rating_router = APIRouter()
@rating_router.post("/rating", response_model=MessageCreateRating)
async def create_rating(rating: RatingCreate, db: AsyncSession = Depends(get_film_db)):
    user_repository = UserRepository(db)
    film_repository = FilmRepository(db)
    rating_average_repository = RatingAverageRepository(db)
    rating_repository = RatingRepository(db)

    rating_average_service = RatingAverageService(rating_average_repository, film_repository)

    rating_service = RatingService(user_repository, film_repository, rating_average_service, rating_repository)

    message = await rating_service.create_rating(
        username=rating.username,
        film_title=rating.film_title,
        rating_user=rating.rating_user,
        review=rating.review,
    )
    return {"message": message}


@rating_router.get("/rating", response_model=Dict[str, Union[FilmRating, List[RatingResponse]]])
async def get_rating(film_title: str, db: AsyncSession = Depends(get_film_db)):
    user_repository = UserRepository(db)
    film_repository = FilmRepository(db)
    rating_average_repository = RatingAverageRepository(db)
    rating_repository = RatingRepository(db)

    rating_average_service = RatingAverageService(rating_average_repository, film_repository)

    rating_service = RatingService(
        user_repository=user_repository,
        film_repository=film_repository,
        rating_average_service=rating_average_service,
        rating_repository=rating_repository
    )
    film_id = await film_repository.get_film_id_by_title(film_title)
    film_rating = await rating_average_service.get_average_web_rating(film_title)
    ratings_and_reviews = await rating_service.get_ratings_and_reviews(film_id)

    return {"film_rating": film_rating, "reviews": ratings_and_reviews}
