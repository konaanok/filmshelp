from typing import List, Optional
from sqlalchemy import join, select
from sqlalchemy.ext.asyncio import AsyncSession
from models.genre_model import genre_table
from models.genre_director_model import genre_director
from models.director_model import director_table

class DirectorRepository:
    __instance: Optional['DirectorRepository'] = None

    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.db = db
            self._initialized = True
        
    async def get_directors_by_genres(self, genre_names: List[str]) -> List[dict]:
        genre_sel = select(genre_table.c.id).where(genre_table.c.name.in_(genre_names))
        genre_result = await self.db.execute(genre_sel)
        genre_ids = [row.id for row in genre_result.fetchall()]

        j = join(genre_director, director_table, genre_director.c.director_id == director_table.c.id)
        sel = (select(director_table.c.id, director_table.c.name).distinct().select_from(j).where(genre_director.c.genre_id.in_(genre_ids)))
        result = await self.db.execute(sel)
        directors = result.fetchall()

        return directors