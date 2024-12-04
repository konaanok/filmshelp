from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from repositories import DirectorRepository
from schemas import DirectorRead, DirectorResponse


class DirectorService:
    __instance: Optional['DirectorService'] = None
    director_rep: Optional[DirectorRepository] = None

    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.director_rep = DirectorRepository(db)
            self._initialized = True
    
    async def get_directors_by_genres(self, genre_names: List[str]) -> List[DirectorRead]:
        directors = await self.director_rep.get_directors_by_genres(genre_names)
        if not directors:
            raise HTTPException(status_code=404, detail="No directors found")
        director_list = [DirectorRead(name=director.name) for director in directors]
        return DirectorResponse(names=director_list)