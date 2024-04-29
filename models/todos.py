from pydantic import BaseModel
from typing import Union
from datetime import datetime

class Todo(BaseModel):
    name: str
    description: str
    complete: bool

class TodoList(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list = []

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None