import os
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from jose import JWTError, jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashPassword(password):
    return pwd_context.hash(password)

def checkPassword(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)

def createAccessToken(data: dict):
    # print(f"--------------------{os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')}----------------------")
    expires_delta = timedelta(minutes = 30)
    print(f"--------------------{expires_delta}----------------------")
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, key= "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7", algorithm= "HS256")
    return encoded_jwt


