from fastapi import FastAPI
# from routes.route import router
from routes.userRoute import userRouter

app = FastAPI()

# app.include_router(router)
app.include_router(userRouter)

