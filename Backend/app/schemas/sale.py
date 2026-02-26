#app/schemas/sale.py
from pydantic import BaseModel
from typing import List, Optional

class saleItemCreate(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

class SaleCreate(BaseModel):
    customer_id: Optional[int] = None
    items: List[saleItemCreate]

class SaleRead(BaseModel):
    sale_id: int
    customer_id: Optional[int] = None
    sale_date: str
    total_amount: float

    class Config:
        orm_mode = True

        