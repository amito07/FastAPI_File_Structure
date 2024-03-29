import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(f"mongodb+srv://{os.getenv('MONGODB_USER')}:{os.getenv('MONGODB_PASSWORD')}@kadodo.10zyvec.mongodb.net/?retryWrites=true&w=majority&appName={os.getenv('APP_NAME')}")

db = client.todo_db

collection_name = db["todo_collection"]