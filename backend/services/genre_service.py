from typing import List
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from repositories import GenreRepository
from schemas import GenreRead


class GenreService:
    def __init__(self, db: AsyncSession):
        self.genre_rep = GenreRepository(db)
    
    async def get_all_genres(self) -> List[GenreRead]:
        genres = await self.genre_rep.get_all_genres()
        if not genres:
            raise HTTPException(status_code=404, detail="No genres found")
        return [{"name": genre.name} for genre in genres]