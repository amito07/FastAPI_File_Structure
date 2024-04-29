from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.users import User
from schema.UserSchema import SignInSchema, SignUpSchema
from utils.function import hash_password, verify_password, create_access_token
from utils.customResponse import InternalServerError, CustomMessage

class UserController():
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    async def singUpUser(self, user: SignUpSchema):
        try:
            userInfo = dict(user)
            hashed_password = hash_password(userInfo['password'])
            userInfo['password'] = hashed_password
            db_user = User(**userInfo)
            self.db_session.add(db_user)
            await self.db_session.flush()
        
        except Exception as e:
            raise InternalServerError()
    
    async def singInUser(self, user: SignInSchema):
        try:
            userInfo = dict(user)
            user = await self.db_session.execute(select(User).filter(User.username == userInfo["username"]))
            userDetails = user.scalar()

            token_data = {
                'username': userDetails.username,
                'email': userDetails.email
            }

            if user:
                if verify_password(userInfo['password'], userDetails.password):
                    token = create_access_token(token_data)
                    user_details = {'user_name': userDetails.username, 'email': userDetails.email, 'access_token': token}
                    return CustomMessage(message='Logged In Successfully', data=user_details) 
                else:
                    raise Exception('Invalid username or email')  
        
        except Exception as e:
            print(e)
            raise InternalServerError()