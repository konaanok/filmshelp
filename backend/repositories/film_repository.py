from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.description_model import description_table
from models.film_model import film_table
 
class FilmRepository:
    def __init__(self, db:AsyncSession):
        self.db = db
    async def get_film_by_description(self, description_name: List[str]) -> List[dict]:
        description_sel = select(description_table.c.id).where(description_table.c.name == description_name)
        description_result = await self.db.execute(description_sel)
        description = description_result.fetchone()
    
        description_id = description.id

        sel = select(film_table).where(film_table.c.description_id == description_id)
        result = await self.db.execute(sel)
        films = result.fetchall()
        return films