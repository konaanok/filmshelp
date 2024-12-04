from typing import List
from pydantic import BaseModel

class DescriptionRead(BaseModel):
    text: str

class DescriptionResponse(BaseModel):
    texts: List[DescriptionRead]