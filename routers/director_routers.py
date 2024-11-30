from fastapi import APIRouter, Depends, Query
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_film_db
from schemas import DirectorRead
from services import DirectorService

director_router = APIRouter()

@director_router.get("/directors", response_model=List[DirectorRead])
async def get_directors(genre_names: List[str] = Query(..., description="Список названий жанров"), db: AsyncSession = Depends(get_film_db)): 
    director_service = DirectorService(db)
    directors = await director_service.get_directors_by_genres(genre_names)
    return directors
