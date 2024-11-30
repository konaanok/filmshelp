from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.genre_repository import GenreRepository
from schemas.genre_schema import GenreRead


class GenreService:
    def __init__(self, db: AsyncSession):
        self.genre_rep = GenreRepository(db)
    
    async def get_all_genres(self) -> List[GenreRead]:
        genres = await self.genre_rep.get_all_genres()
        if not genres:
            return None
        return [{"name": genre.name} for genre in genres]