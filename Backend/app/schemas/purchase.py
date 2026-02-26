#app/schemas/purchase_schema.py

from pydantic import BaseModel
from typing import List, Optional

class PurchaseItem(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

class PurchaseCreate(BaseModel):
    supplier_id: Optional[int] = None
    total_amount: float
    items: List[PurchaseItem]

class Purchase(BaseModel):
    purchase_id: int
    supplier_id: Optional[int] = None
    purchase_date: str
    total_amount: float
    items: List[PurchaseItem]

    class Config:
        orm_mode = True

        