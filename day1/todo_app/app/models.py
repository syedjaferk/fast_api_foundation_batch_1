from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Todo(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoDB(Todo):
    id: str

    class Config:
        orm_mode = True
