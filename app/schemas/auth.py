from pydantic import BaseModel, EmailStr

class UserSignup(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone: str 

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    