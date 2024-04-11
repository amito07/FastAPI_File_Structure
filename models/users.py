from pydantic import BaseModel

class SignUpBaseModel(BaseModel):
    username: str
    password: str
    email: str
    full_name: str

class SignInModel(BaseModel):
    username: str
    password: str

