from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories import FilmRepository
from schemas import FilmRead


class FilmService:
    def __init__(self, db: Session):
        self.film_rep = FilmRepository(db)
    
    async def get_film_by_description(self, description_name: str) -> List[FilmRead]:
        films = await self.film_rep.get_film_by_description(description_name)
        if not films:
            raise HTTPException(status_code=404, detail="No films found")
        return [{"year": film.year, "title": film.title} for film in films]