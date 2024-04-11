from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from utils.customResponse import CustomMessage
from fastapi import Request

def todo_list(request: Request):
    user = request.state.user
    print(f'-----------------User From Todo {user}-------------------')
    todos = list_serial(collection_name.find())
    return CustomMessage(message='List of Todos', data=todos)

def create_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return CustomMessage(message='Todo Created')


def update_todo(todo_id: str, todo: Todo):
    collection_name.update_one({'_id': ObjectId(todo_id)}, {'$set': dict(todo)})
    return CustomMessage(message='Todo Updated')

def delete_todo(todo_id: str):
    collection_name.delete_one({'_id': ObjectId(todo_id)})
    return CustomMessage(message='Todo Deleted')