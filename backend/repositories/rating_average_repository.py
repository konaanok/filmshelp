from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, Any
from models.rating_model import rating_average_table


class RatingAverageRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_average_rating(self, film_id: int) -> Optional[Any]:
        query = (
            select(
                rating_average_table.c.rating_web,
                rating_average_table.c.rating_average,
            ).where(rating_average_table.c.film_id == film_id)
        )
        result = await self.db.execute(query)
        return result.fetchone()

    async def get_rating_data_by_film_id(self, film_id: int) -> Optional[tuple]:
        query = select(
            (rating_average_table.c.rating_average).label("average_rating"),
            (rating_average_table.c.rating_count).label("rating_count"),
        ).where(rating_average_table.c.film_id == film_id)
        result = await self.db.execute(query)
        return result.fetchone()

    async def update_rating_average(self, film_id: int, new_avg_rating: float, new_rating_count: int):
        query = (
            update(rating_average_table)
            .where(rating_average_table.c.film_id == film_id)
            .values(rating_average=new_avg_rating, rating_count=new_rating_count)
        )
        await self.db.execute(query)
    
