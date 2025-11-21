from enum import Enum
from typing import Dict, List
from pydantic import BaseModel


class UserRequest(BaseModel):
    email: str
    password: str


class UserLogIn(BaseModel):
    user_token: str

class UserSchema(BaseModel):
    email: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
