from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_film_db
from schemas.genre_schema import GenreRead
from services.genre_service import GenreService

genre_router = APIRouter()

@genre_router.get("/genres", response_model=List[GenreRead])
async def get_genres(db: AsyncSession = Depends(get_film_db)):
    genre_service = GenreService(db)
    genres = await genre_service.get_all_genres()
    if not genres:
        raise HTTPException(status_code=404, detail="No genres found")
    return genres
