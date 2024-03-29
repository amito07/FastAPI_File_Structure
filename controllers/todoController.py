from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from utils.customResponse import CustomMessage

def todo_list():
    todos = list_serial(collection_name.find())
    return CustomMessage(message='List of Todos', data=todos)

def create_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return CustomMessage(message='Todo Created')

