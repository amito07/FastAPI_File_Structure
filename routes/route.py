import os
from fastapi import APIRouter
from models.todos import Todo

from controllers.todoController import todo_list, create_todo
router = APIRouter()

#GET Requests Method

@router.get("/")
async def get_todos():
    return todo_list()


#POST Requests Method

@router.post("/")
async def post_todos(todo:Todo):
    return create_todo(todo)