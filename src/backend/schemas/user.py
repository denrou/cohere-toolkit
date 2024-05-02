import datetime
from typing import Optional

from pydantic import BaseModel, validator, Field
from backend.services.authentication.utils import hash_and_salt_password


class UserBase(BaseModel):
    fullname: str
    email: Optional[str] = None


class User(UserBase):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True

class UserPassword(BaseModel):
    password: Optional[str] = None
    hashed_password: Optional[bytes] = None

    def __init__(self, **data):
        password = data.pop("password")
        
        if password is not None:
            data["hashed_password"] = hash_and_salt_password(password)
        
        super().__init__(**data)

class CreateUser(UserBase, UserPassword):
    pass

class UpdateUser(UserPassword):
    fullname: Optional[str] = None
    email: Optional[str] = None 

class DeleteUser(BaseModel):
    pass
