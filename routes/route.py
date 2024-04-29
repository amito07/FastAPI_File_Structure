import os
from fastapi import APIRouter, Depends, Request, Path, Query, File, UploadFile, Form, BackgroundTasks
from models.todos import Todo
from authMiddlware.middlewareFunction import get_current_user
from typing_extensions import Annotated
from typing import Union
from models.todos import TodoList, Item
from fastapi.encoders import jsonable_encoder

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

@router.get("/items/{item_id}")
async def read_items(*, item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],q:str, size: Annotated[float, Query(gt=0, lt=10.5)]):
    results = {"item_id": item_id}
    if q:
        results.update({'q':q})
    return results

@router.post("/items")
async def create_item(item: TodoList):
    return item

@router.post("/files/")
async def create_file(file: Annotated[bytes, File()], campaign_name: Annotated[str, Form()]):
    return {'file_size': len(file)}
@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


@router.post("/Items/{id}")
async def create_items(id: str, item: Item):
    fake_db = {}
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    return fake_db

async def common_parameters(q: Union[str, None] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@router.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons

def write_notification(email: str, message: Annotated[str, None] = None):
    with open("log.txt", "w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@router.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}





