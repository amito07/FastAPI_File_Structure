from pydantic import BaseModel


class SignUpSchema(BaseModel):
    username: str
    password: str
    email: str

class SignInSchema(BaseModel):
    username: str
    password: str

