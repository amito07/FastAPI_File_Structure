import os
from fastapi import APIRouter, Depends, Request
from models.todos import Todo
from authMiddlware.middlewareFunction import get_current_user

from controllers.todoController import todo_list, create_todo
router = APIRouter(tags=['Todo'])

#GET Requests Method

@router.get("/", dependencies=[Depends(get_current_user)])
async def get_todos(request: Request):
    print(f'----------------Request {request}----------------------------')
    return await todo_list(request)


#POST Requests Method

@router.post("/")
async def post_todos(todo:Todo):
    return create_todo(todo)