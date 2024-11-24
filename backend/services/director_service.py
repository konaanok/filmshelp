from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.director_repository import DirectorRepository
from schemas.director_schema import DirectorRead


class DirectorService:
    def __init__(self, db: AsyncSession):
        self.director_rep = DirectorRepository(db)
    
    async def get_directors_by_genres(self, genre_names: List[str]) -> List[DirectorRead]:
        directors = await self.director_rep.get_directors_by_genres(genre_names)
        if not directors:
            return None
        return [{"name": director.name} for director in directors]