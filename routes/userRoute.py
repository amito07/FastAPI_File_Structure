import os
from fastapi import APIRouter, Depends
# from models.users import SignUpBaseModel, SignInModel
from schema.UserSchema import SignUpSchema, SignInSchema
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db

from controllers.userController import signUpUser, signInUser
userRouter = APIRouter(tags=['User'], prefix='/user')

#POST Requests Method

@userRouter.post("/signUp")
async def createUser(user:SignUpSchema, db: AsyncSession = Depends(get_db)):
    print(f'---------------User: {user}-------------------------')
    result = await signUpUser(user, db)
    return result


#POST Requests Method

@userRouter.post("/signIn") 
async def loginUser(user:SignInSchema):
    return await signInUser(user)