from typing import List, Optional
from fastapi import HTTPException, status
from repositories import FilmRepository, RatingRepository, UserRepository
from schemas import RatingResponse, MessageCreateRating
from services import RatingAverageService
from sqlalchemy.ext.asyncio import AsyncSession

class RatingService:
    _instance: Optional['RatingService'] = None
    user_repository: Optional[UserRepository] = None
    film_repository: Optional[FilmRepository] = None
    rating_average_service: Optional[RatingAverageService] = None
    rating_repository: Optional[RatingRepository] = None
    
    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.user_repository = UserRepository(db)
            self.film_repository = FilmRepository(db)
            self.rating_average_service = RatingAverageService(db)
            self.rating_repository = RatingRepository(db)
            self._initialized = True
    
    async def get_ratings_and_reviews(self, film_id: int) -> List[RatingResponse]:
        ratings = await self.rating_repository.get_user_ratings(film_id)
        return [RatingResponse(username=rating.username, rating_user=rating.rating_user, review=rating.review) for rating in ratings]
    
    async def create_rating(self, username: str, film_title: str, rating_user: int, review: str) -> MessageCreateRating:
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
        return MessageCreateRating(message="Спасибо за отзыв!")
