import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
load_dotenv()

client = AsyncIOMotorClient(f"mongodb+srv://amitmandal:ko6elt1FXX3xJWkP@kadodo.mnspvfq.mongodb.net/?retryWrites=true&w=majority&appName=Kadodo")

db = client.todo_db

collection_name = db["todo_collection"]
user_collection = db["user_collection"]

