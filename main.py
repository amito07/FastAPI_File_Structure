from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes.userRoute import userRouter
from config.database import engine, Base

app = FastAPI()

##This function will be called before the application is initialized
@asynccontextmanager
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
app.include_router(userRouter)

