from fastapi import APIRouter, Depends, Query
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_film_db
from schemas import DescriptionRead
from services import DescriptionService

description_router = APIRouter()

@description_router.get("/descriptions", response_model=List[DescriptionRead])
async def get_descriptions(director_names: List[str] = Query(..., description="Список имён режиссёров"), db: AsyncSession = Depends(get_film_db)):
    description_service = DescriptionService(db)
    descriptions = await description_service.get_description_by_directors(director_names)
    return descriptions