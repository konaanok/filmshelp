from typing import List
from sqlalchemy.orm import Session
from repositories.film_repository import FilmRepository
from schemas.film_schema import FilmRead


class FilmService:
    def __init__(self, db: Session):
        self.film_rep = FilmRepository(db)
    
    async def get_film_by_description(self, description_name: str) -> List[FilmRead]:
        films = await self.film_rep.get_film_by_description(description_name)
        if not films:
            return None
        return [{"year": film.year, "title": film.title} for film in films]