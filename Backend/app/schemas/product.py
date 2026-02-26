#app/schemas/product.py

from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    product_name: str
    category: Optional[str] = None
    barcode: Optional[str] = None
    purchase_price: float
    selling_price: float
    stock_quantity: int
    description: Optional[str] = None
    
class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    category: Optional[str] = None
    barcode: Optional[str] = None
    purchase_price: Optional[float] = None
    selling_price: Optional[float] = None
    stock_quantity: Optional[int] = None
    description: Optional[str] = None

class ProductRead(BaseModel):
    product_id: int
    product_name: str
    category: Optional[str] = None
    barcode: Optional[str] = None
    purchase_price: float
    selling_price: float
    stock_quantity: int
    description: Optional[str] = None

    class Config:
        orm_mode = True

        