from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_film_db
from schemas.film_schema import FilmRead
from services.film_service import FilmService

film_router = APIRouter()

@film_router.get("/films", response_model=List[FilmRead])
async def get_films(description_name: str = Query(...), db: AsyncSession = Depends(get_film_db)):
    film_service = FilmService(db)
    films = await film_service.get_film_by_description(description_name)
    if not films:
        raise HTTPException(status_code=404, detail="No films found")
    return films
