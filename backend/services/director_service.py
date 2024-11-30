from typing import List
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from repositories import DirectorRepository
from schemas import DirectorRead


class DirectorService:
    def __init__(self, db: AsyncSession):
        self.director_rep = DirectorRepository(db)
    
    async def get_directors_by_genres(self, genre_names: List[str]) -> List[DirectorRead]:
        directors = await self.director_rep.get_directors_by_genres(genre_names)
        if not directors:
            raise HTTPException(status_code=404, detail="No directors found")
        return [{"name": director.name} for director in directors]