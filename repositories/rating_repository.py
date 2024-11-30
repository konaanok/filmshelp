from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Any
from models import rating_table

class RatingRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_ratings(self, film_id: int) -> List[Any]:
        query = (
            select(
                rating_table.c.rating_user,
                rating_table.c.review,
                rating_table.c.username,
            ).where(rating_table.c.film_id == film_id)
        )
        result = await self.db.execute(query)
        return result.fetchall()
    
    async def add_user_rating(self, film_id: int, rating_user: int, review: str, username: str):
        query = insert(rating_table).values(
            film_id=film_id, rating_user=rating_user, review=review, username=username
        )
        await self.db.execute(query)

