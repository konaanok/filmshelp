from pydantic import BaseModel

class FilmRead(BaseModel):
    title: str
    year: int

    class Config:
        orm_mode = True