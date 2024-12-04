from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.description_model import description_table
from models.film_model import film_table

class FilmRepository:
    __instance: Optional['FilmRepository'] = None

    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.db = db
            self._initialized = True

    async def get_film_by_description(self, description_name: List[str]) -> List[dict]:
        description_sel = select(description_table.c.id).where(description_table.c.name == description_name)
        description_result = await self.db.execute(description_sel)
        description = description_result.fetchone()
    
        description_id = description.id

        sel = select(film_table).where(film_table.c.description_id == description_id)
        result = await self.db.execute(sel)
        films = result.fetchall()
        return films
    
    async def get_film_id_by_title(self, title: str) -> int:
        query = select(film_table.c.id).where(film_table.c.title == title)
        result = await self.db.execute(query)
        film = result.fetchone()
        return film.id if film else None

