from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from utils.customResponse import CustomMessage
from fastapi import Request

async def todo_list(request: Request):
    user = request.state.user
    print(f'-----------------User From Todo {user}-------------------')
    todos = await collection_name.find().to_list(length=100)
    todos = list_serial(todos)
    return CustomMessage(message='List of Todos', data=todos)

async def create_todo(todo: Todo):
    await collection_name.insert_one(dict(todo))
    return CustomMessage(message='Todo Created')


async def update_todo(todo_id: str, todo: Todo):
    await collection_name.update_one({'_id': ObjectId(todo_id)}, {'$set': dict(todo)})
    return CustomMessage(message='Todo Updated')

async def delete_todo(todo_id: str):
    await collection_name.delete_one({'_id': ObjectId(todo_id)})
    return CustomMessage(message='Todo Deleted')