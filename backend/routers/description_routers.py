from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_film_db
from schemas.description_schema import DescriptionRead
from services.description_service import DescriptionService

description_router = APIRouter()

@description_router.get("/", response_model=List[DescriptionRead])
async def get_descriptions(director_names: List[str] = Query(..., description="Список имён режиссёров"), db: AsyncSession = Depends(get_film_db)):
    description_service = DescriptionService(db)
    descriptions = await description_service.get_description_by_directors(director_names)
    if not descriptions:
        raise HTTPException(status_code=404, detail="No descriptions found")
    return descriptions