from typing import List
from fastapi import HTTPException, status
from repositories.film_repository import FilmRepository
from repositories.rating_repository import RatingRepository
from repositories.user_repository import UserRepository
from schemas.rating_schema import RatingResponse
from services.rating_average_service import RatingAverageService


class RatingService:
    def __init__(self, user_repository: UserRepository, film_repository: FilmRepository, rating_average_service: RatingAverageService, rating_repository: RatingRepository):
        self.user_repository = user_repository
        self.film_repository = film_repository
        self.rating_average_service = rating_average_service
        self.rating_repository = rating_repository

    async def get_ratings_and_reviews(self, film_id: int) -> List[RatingResponse]:
        ratings = await self.rating_repository.get_user_ratings(film_id)
        return [RatingResponse(username=rating.username, rating_user=rating.rating_user, review=rating.review) for rating in ratings]
    

    async def create_rating(self, username: str, film_title: str, rating_user: int, review: str) -> str:
        user_id = await self.user_repository.get_user_id_by_username(username)
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        film_id = await self.film_repository.get_film_id_by_title(film_title)
        if not film_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Film not found",
            )
        await self.rating_average_service.update_average_rating(film_id, rating_user)
        await self.rating_repository.add_user_rating(film_id, rating_user, review, username)
        return "Спасибо за отзыв!"
