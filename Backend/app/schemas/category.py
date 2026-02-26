#app/schemas/category.py
from pydantic import BaseModel
from typing import Optional 

class CategoryCreate(BaseModel):
    category_name: str
    description: Optional[str] = None

class CategoryUpdate(BaseModel):
    category_name: Optional[str] = None
    description: Optional[str] = None

class CategoryRead(BaseModel):
    category_id: int
    category_name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

        