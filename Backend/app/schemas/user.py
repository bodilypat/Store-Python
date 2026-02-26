# app/schemas/user.py Pydantic schemas for User model
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: Optional[str] = None
    phone_number: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None
    phone_number: Optional[str] = None

class UserRead(UserBase):
    user_id: int
    created_at: str

    class Config:
        orm_mode = True


