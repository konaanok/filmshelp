from typing import List
from pydantic import BaseModel

class GenreRead(BaseModel):
    name: str

class GenreResponse(BaseModel):
    names: List[GenreRead]