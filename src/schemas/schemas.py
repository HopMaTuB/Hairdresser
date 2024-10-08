from pydantic import BaseModel, EmailStr,Field
from datetime import datetime

class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: EmailStr
    password: str = Field(min_length=6, max_length=10)

class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    username: str 
    email: EmailStr
    password: str 
    detail: str = "User successfully created"

class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RequestEmail(BaseModel):
    email: EmailStr