from fastapi import APIRouter, Depends
from schema.UserSchema import SignUpSchema, SignInSchema
from controllers.userController import UserController
from config.database import async_session



userRouter = APIRouter(tags=['User'], prefix='/user')

#SignUp Requests

@userRouter.post("/signUp")
async def createUser(user:SignUpSchema):
    async with async_session() as session:
        async with session.begin():
            user_info = UserController(session)
            return await user_info.singUpUser(user)


#SignIn Requests

@userRouter.post("/signIn") 
async def loginUser(user:SignInSchema):
    async with async_session() as session:
        async with session.begin():
            user_info = UserController(session)
            return await user_info.singInUser(user)