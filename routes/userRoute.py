import os
from fastapi import APIRouter
from models.users import SignUpBaseModel, SignInModel

from controllers.userController import signUpUser, signInUser
userRouter = APIRouter(tags=['User'], prefix='/user')

#POST Requests Method

@userRouter.post("/signUp")
async def createUser(user:SignUpBaseModel):
    return signUpUser(user)


#POST Requests Method

@userRouter.post("/signIn") 
async def loginUser(user:SignInModel):
    return await signInUser(user)