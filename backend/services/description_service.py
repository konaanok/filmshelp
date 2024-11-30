from sqlalchemy.ext.asyncio import AsyncSession
from repositories.description_repository import DescriptionRepository
from typing import List
from schemas.description_schema import DescriptionRead

class DescriptionService:
    def __init__(self, db:AsyncSession):
        self.description_rep = DescriptionRepository(db)
    
    async def get_description_by_directors(self, director_names: List[str]) -> List[DescriptionRead]:
        descriptions = await self.description_rep.get_description_by_directors(director_names)
        if not descriptions:
            return None
        return [{"text": description.text} for description in descriptions]