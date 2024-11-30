from pydantic import BaseModel

class GenreRead(BaseModel):
    name: str

    class Config:
        orm_mode = True