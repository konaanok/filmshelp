from pydantic import BaseModel

class DirectorRead(BaseModel):
    name: str

    class Config:
        orm_mode = True