from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_film_db
from schemas import FilmResponse
from services import FilmService

film_router = APIRouter()

@film_router.get("/films", response_model=FilmResponse)
async def get_films(description_name: str = Query(...), db: AsyncSession = Depends(get_film_db)):
    film_service = FilmService(db)
    films = await film_service.get_film_by_description(description_name)
    return films
