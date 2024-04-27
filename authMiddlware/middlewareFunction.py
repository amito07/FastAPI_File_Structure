# import os
# from fastapi import Depends, Request, HTTPException
# from typing import Optional
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from utils.customResponse import UnauthorizedError
# from jose import jwt
# from config.database import user_collection

# security = HTTPBearer()
# async def get_current_user(request: Request, token: HTTPAuthorizationCredentials = Depends(security)) -> Optional[str]:
#     if not token:
#         raise UnauthorizedError()
    
            
#     bearer_token = token.credentials


#     if bearer_token is None:
#         raise UnauthorizedError()
        
#     try:
#         payload = jwt.decode(bearer_token, os.getenv('SECRET_KEY'), algorithms=[os.getenv('ALGORITHM')])
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token is expired")

#     user = await user_collection.find_one({'email': payload['email']})

#     if user is None:
#         raise UnauthorizedError()
    
#     userInfo = {
#         "username": user['username'],
#         "email": user['email'],
#     }
    
#     request.state.user = userInfo

#     return userInfo