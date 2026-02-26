# app/schemas/auth.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: Optional[str] = 'cashier'
    phone_number: Optional[str] = None

class UserRead(BaseModel):
    user_id: int
    full_name: str
    email: EmailStr
    role: str
    phone_number: Optional[str] = None

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

class TokenPayload(BaseModel):
    user_id: int
    role: Optional[str] = None

    