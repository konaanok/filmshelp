from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_film_db
from schemas.director_schema import DirectorRead
from services.director_service import DirectorService

director_router = APIRouter()

@director_router.get("/directors", response_model=List[DirectorRead])
async def get_directors(genre_names: List[str] = Query(..., description="Список названий жанров"), db: AsyncSession = Depends(get_film_db)): 
    director_service = DirectorService(db)
    directors = await director_service.get_directors_by_genres(genre_names)
    if not directors:
        raise HTTPException(status_code=404, detail="No directors found")
    return directors
