from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import join, select
from models.director_model import director_table
from models.description_model import description_table
from models.director_description_model import director_description

class DescriptionRepository:
    __instance: Optional['DescriptionRepository'] = None

    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.db = db
            self._initialized = True

    async def get_description_by_directors(self, director_names: List[str]) -> List[dict]:
        director_sel = select(director_table.c.id).where(director_table.c.name.in_(director_names))
        director_result = await self.db.execute(director_sel)
        director_ids = [row.id for row in director_result.fetchall()]
    
        j = join(director_description, description_table, director_description.c.description_id == description_table.c.id)
        sel = select(description_table).distinct().select_from(j).where(director_description.c.director_id.in_(director_ids))
        result = await self.db.execute(sel)
        descriptions = result.fetchall()

        return descriptions