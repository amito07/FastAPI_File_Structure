from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from routes.userRoute import userRoute
from routes.route import router
from config.database import client
app = FastAPI()

app.include_router(router)
app.include_router(userRoute)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)