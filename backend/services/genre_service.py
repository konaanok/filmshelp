from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from repositories import GenreRepository
from schemas import GenreRead, GenreResponse


class GenreService:
    __instance: Optional['GenreService'] = None
    genre_rep: Optional[GenreRepository] = None

    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.genre_rep = GenreRepository(db)
            self._initialized = True
    
    async def get_all_genres(self) -> List[GenreRead]:
        genres = await self.genre_rep.get_all_genres()
        if not genres:
            raise HTTPException(status_code=404, detail="No genres found")
        genre_list = [GenreRead(name=genre.name) for genre in genres]
        return GenreResponse(names=genre_list)