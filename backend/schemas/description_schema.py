from pydantic import BaseModel

class DescriptionRead(BaseModel):
    text: str

    class Config:
        orm_mode = True