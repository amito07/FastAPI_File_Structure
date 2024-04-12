from models.users import User, LoginUser
from config.database import user_collection
from utils.customResponse import CustomMessage
from utils.function import hashPassword, checkPassword, createAccessToken
from utils.customResponse import CustomMessage
from fastapi import HTTPException


def signUpUser(user: User):
    try:
        print(dict(user))
        user_info = dict(user)
        hash_password = hashPassword(user_info["password"])
        user_info["password"] = hash_password
        user_collection.insert_one(dict(user_info))
        return CustomMessage(message='User Created')

    except Exception as e:
        print(e)

def userLogin(user: LoginUser):
    try: 
        print(dict(user))
        userInfo = dict(user)
        userExist = user_collection.find_one({'email': userInfo["email"]})
        if not userExist:
            raise HTTPException(status_code=404, detail={'message': 'User does not exist'})
        checked_password = checkPassword(userInfo['password'], userExist["password"])
        if not checked_password:
            raise HTTPException(status_code=404, detail={'message': 'Username or password incorrect'})
        access_token = createAccessToken(userInfo)
        userInfo['access_token'] = access_token
        del userInfo['password']
        return CustomMessage(message='User Created', data= userInfo)
    except HTTPException as e:
        print(e)



