from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_film_db
from schemas.description_schema import DescriptionRead
from schemas.director_schema import DirectorRead
from schemas.film_schema import FilmRead
from schemas.genre_schema import GenreRead
from services.description_service import DescriptionService
from services.director_service import DirectorService
from services.film_service import FilmService
from services.genre_service import GenreService

# rating_router = APIRouter()

# @rating_router.post("/", response_model=MessageCreateRating)
# async def create_rating(rating: RatingCreate, db: AsyncSession = Depends(get_film_db)):
#     user_sel = select(user_table.c.id).where(user_table.c.username == rating.username)
#     user_result = await db.execute(user_sel)
#     user = user_result.fetchone()

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )

#     film_sel = select(film_table.c.id).where(film_table.c.title == rating.film_title)
#     film_result = await db.execute(film_sel)
#     film = film_result.fetchone()

#     film_id = film[0]

#     rating_sel = select(
#         (rating_average_table.c.rating_average).label('average_rating'),
#         (rating_average_table.c.rating_count).label('rating_count')
#     ).where(rating_average_table.c.film_id == film_id)
    
#     rating_result = await db.execute(rating_sel)
#     rating_data = rating_result.fetchone()

#     current_avg_rating, current_rating_count = rating_data

#     new_avg_rating = (current_avg_rating * current_rating_count + rating.rating_user) / (current_rating_count + 1)
#     new_rating_count = current_rating_count + 1

#     sel_update = update(rating_average_table).where(rating_average_table.c.film_id == film_id).values(
#         rating_average=new_avg_rating,
#         rating_count=new_rating_count
#     )
#     await db.execute(sel_update)

#     stmt_insert = insert(rating_table).values(
#         film_id=film_id,
#         rating_user=rating.rating_user,
#         review=rating.review,
#         username=rating.username,
#     )
#     await db.execute(stmt_insert)
#     await db.commit()

#     return {"message": "Спасибо за отзыв!"}


# @rating_router.get("/", response_model=Dict[str, Union[FilmRating, List[RatingResponse]]])
# async def get_rating(film_title: str = Query(..., description="Название фильма"), db: AsyncSession = Depends(get_film_db)):
#     film_sel = select(film_table.c.id).where(film_table.c.title == film_title)
#     film_result = await db.execute(film_sel)
#     film = film_result.fetchone()

#     film_id = film.id

#     rating_sel = select(rating_average_table).where(rating_average_table.c.film_id == film_id)
#     rating_result = await db.execute(rating_sel)
#     rating = rating_result.fetchone()

#     if not rating:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")

#     sel = select(
#         rating_table.c.rating_user,
#         rating_table.c.review,
#         rating_table.c.username,
#         rating_average_table.c.rating_average,
#         rating_average_table.c.rating_web 
#     ).join(
#         rating_average_table, rating_table.c.film_id == rating_average_table.c.film_id
#     ).where(rating_table.c.film_id == film_id)
#     result = await db.execute(sel)
#     ratings = result.fetchall()

#     return {
#         "film_rating": FilmRating(rating_web=rating.rating_web, rating_average=rating.rating_average),
#         "reviews": [RatingResponse(username=rating.username, rating_user=rating.rating_user, review=rating.review) for rating in ratings]
#     }
