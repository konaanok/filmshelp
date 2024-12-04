from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_film_db
from schemas import GenreResponse
from services import GenreService

genre_router = APIRouter()

@genre_router.get("/genres", response_model=GenreResponse)
async def get_genres(db: AsyncSession = Depends(get_film_db)):
    genre_service = GenreService(db)
    genres = await genre_service.get_all_genres()
    return genres