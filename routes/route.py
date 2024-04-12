import os
from fastapi import APIRouter, Depends
from models.todos import Todo
from dotenv import load_dotenv
from authentication.auth import oauth2_schema
load_dotenv()

from controllers.todoController import todo_list, create_todo
router = APIRouter(prefix='/api/v1', tags=['Todo'])

#GET Requests Method

@router.get("/todolist")
async def get_todos(token: str = Depends(oauth2_schema)):
    return todo_list()


#POST Requests Method

@router.post("/create-todo")
async def post_todos(todo:Todo):
    return create_todo(todo)