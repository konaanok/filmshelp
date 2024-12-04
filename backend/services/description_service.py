from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from repositories import DescriptionRepository
from typing import List, Optional
from schemas import DescriptionRead, DescriptionResponse

class DescriptionService:
    __instance: Optional['DescriptionService'] = None
    description_rep: Optional[DescriptionRepository] = None

    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.description_rep = DescriptionRepository(db)
            self._initialized = True
    
    async def get_description_by_directors(self, director_names: List[str]) -> List[DescriptionRead]:
        descriptions = await self.description_rep.get_description_by_directors(director_names)
        if not descriptions:
            raise HTTPException(status_code=404, detail="No descriptions found")
        description_list = [DescriptionRead(text=description.text) for description in descriptions]
        return DescriptionResponse(texts=description_list)