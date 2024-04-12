from fastapi import APIRouter
from models.users import User, LoginUser
from controllers.userController import signUpUser, userLogin

userRoute = APIRouter(prefix='/api/v1/users', tags=["Users"])

@userRoute.post("/sign-up")
async def signUp(user: User):
    return signUpUser(user)

@userRoute.post("/login")
def signIn(user: LoginUser):
    return userLogin(user)


