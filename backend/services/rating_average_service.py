from typing import Optional
from repositories import FilmRepository, RatingAverageRepository
from fastapi import HTTPException, status
from schemas import FilmRating
from sqlalchemy.ext.asyncio import AsyncSession


class RatingAverageService:
    _instance: Optional['RatingAverageService'] = None
    rating_average_repository: Optional[RatingAverageRepository] = None
    film_repository: Optional[FilmRepository] = None

    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.rating_average_repository = RatingAverageRepository(db)
            self.film_repository = FilmRepository(db)
            self._initialized = True

    async def get_average_web_rating(self, film_title: str) -> FilmRating:
        film_id = await self.film_repository.get_film_id_by_title(film_title)
        if not film_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Film not found")
        rating = await self.rating_average_repository.get_average_rating(film_id)
        if not rating:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
        return FilmRating(rating_web=rating.rating_web, rating_average=rating.rating_average)
    
    async def update_average_rating(self, film_id: int, new_user_rating: int):
        rating_data = await self.rating_average_repository.get_rating_data_by_film_id(film_id)
        if not rating_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Rating not found",
            )
        current_avg_rating, current_rating_count = rating_data
        new_avg_rating = (current_avg_rating * current_rating_count + new_user_rating) / (current_rating_count + 1)
        new_rating_count = current_rating_count + 1
        await self.rating_average_repository.update_rating_average(film_id, new_avg_rating, new_rating_count)

    
    
