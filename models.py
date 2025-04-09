from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str

class Movie(BaseModel):
    id:int
    user_id: int
    title:str
    is_animated: bool
    nominated: bool
    nomination_year: Optional[int]
    id_deleted: bool = False
