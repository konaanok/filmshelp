from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from repositories import FilmRepository
from schemas import FilmRead, FilmResponse

class FilmService:
    _instance: Optional['FilmService'] = None
    db: Optional[AsyncSession] = None
    film_rep: Optional[FilmRepository] = None

    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.film_rep = FilmRepository(db)
            self._initialized = True
    
    async def get_film_by_description(self, description_name: str) -> List[FilmRead]:
        films = await self.film_rep.get_film_by_description(description_name)
        if not films:
            raise HTTPException(status_code=404, detail="No films found")
        film_list = [FilmRead(year=film.year, title=film.title) for film in films]
        return FilmResponse(films=film_list)