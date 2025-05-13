from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    code: int
    id_deleted: bool = False

class MovieCreate(BaseModel):
    user_id: int
    title: str
    is_animated:  bool
    nominated: bool
    nominated:  Optional[int] = False