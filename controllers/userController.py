from models.users import SignUpBaseModel, SignInModel
from utils.function import hash_password, verify_password, create_access_token
from config.database import user_collection
from utils.customResponse import InternalServerError, CustomMessage
def signUpUser(user: SignUpBaseModel):
    try:
        userInfo = dict(user)
        hashed_password = hash_password(userInfo['password'])
        userInfo['password'] = hashed_password
        user_collection.insert_one(userInfo)
        return CustomMessage(message='User Created')
    except Exception as e:
        raise InternalServerError()

def signInUser(user: SignInModel):
    try:
        userInfo = dict(user)
        user = user_collection.find_one({'username': userInfo['username']})
        if user:
            if verify_password(userInfo['password'], user["password"]):
                del user['password']
                del user['_id']
                token = create_access_token(user)
                user_details = {'user_name': user['username'], 'email': user['email'], 'access_token': token}
                return CustomMessage(message='Logged In Successfully', data=user_details) 
            else:
                raise Exception('Invalid username or email')                
    except Exception as e:
        print(e)
        raise InternalServerError()