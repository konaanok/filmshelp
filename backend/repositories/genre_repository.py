from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from models.genre_model import genre_table
from sqlalchemy import select


class GenreRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    async def get_all_genres(self) -> List[dict]:
        sel = select(genre_table)
        result = await self.db.execute(sel)
        genres = result.fetchall()
        return genres