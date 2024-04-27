# from models.users import SignUpBaseModel, SignInModel
from utils.function import hash_password
# from config.database import user_collection
from fastapi import Depends
from config.database import get_db
from models.users import User
from utils.customResponse import InternalServerError, CustomMessage
from schema.UserSchema import SignInSchema, SignUpSchema
from sqlalchemy.ext.asyncio import AsyncSession


async def signUpUser(user: SignUpSchema, db: AsyncSession = Depends(get_db)):
    try:
        userInfo = dict(user)
        hashed_password = hash_password(userInfo['password'])
        userInfo['password'] = hashed_password
        db_user = User(**userInfo)
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return CustomMessage(message='User Created')
    except Exception as e:
        raise InternalServerError()

async def signInUser(user: SignUpSchema, db: AsyncSession = Depends(get_db)):
    try:
        userInfo = dict(user)

        # result =  db.query(User).filter(User.username == userInfo["username"]).first()
        # result = await db.query(User).filter(User.username == userInfo["username"]).first()
        result = db.get_one(User, User.username == userInfo["username"])
        # db.get_one(User, )
        print(f'---------user: {result}----------------')
        # user = await user_collection.find_one({'username': userInfo['username']})
        # if user:
        #     if verify_password(userInfo['password'], user["password"]):
        #         del user['password']
        #         del user['_id']
        #         token = create_access_token(user)
        #         user_details = {'user_name': user['username'], 'email': user['email'], 'access_token': token}
        #         return CustomMessage(message='Logged In Successfully', data=user_details) 
        #     else:
        #         raise Exception('Invalid username or email')                
    except Exception as e:
        print(e)
        raise InternalServerError()
    return user