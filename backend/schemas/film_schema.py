from typing import List
from pydantic import BaseModel

class FilmRead(BaseModel):
    title: str
    year: int

class FilmResponse(BaseModel):
    films: List[FilmRead]