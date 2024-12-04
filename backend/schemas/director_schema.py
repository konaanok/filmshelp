from typing import List
from pydantic import BaseModel

class DirectorRead(BaseModel):
    name: str

class DirectorResponse(BaseModel):
    names: List[DirectorRead]