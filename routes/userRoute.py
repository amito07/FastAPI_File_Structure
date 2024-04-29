import os
from fastapi import APIRouter, Query
from models.users import SignUpBaseModel, SignInModel
from typing_extensions import Annotated
from typing import Union

from controllers.userController import signUpUser, signInUser
userRouter = APIRouter(tags=['User'], prefix='/user')

#POST Requests Method

@userRouter.post("/signUp")
async def createUser(user:SignUpBaseModel):
    return await signUpUser(user)


#POST Requests Method

@userRouter.post("/signIn") 
async def loginUser(user:SignInModel):
    return await signInUser(user)


@userRouter.get("/users/")
async def user_list(q: Annotated[Union[str,None], Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q: 
        results.update({"q": q})
    return results

