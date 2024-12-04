from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from models.genre_model import genre_table
from sqlalchemy import select

class GenreRepository:
    __instance: Optional['GenreRepository'] = None

    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.db = db
            self._initialized = True
    
    async def get_all_genres(self) -> List[dict]:
        sel = select(genre_table)
        result = await self.db.execute(sel)
        genres = result.fetchall()
        return genres