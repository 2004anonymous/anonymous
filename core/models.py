from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    name : str
    email : EmailStr
    password : str

class ResUserModel(BaseModel):
    name : str
    email : EmailStr