#app/schemas/inventory_schema.py
from pydantic import BaseModel
from typing import Optional

class InventoryItem(BaseModel):
    product_id: Optional[int]
    product_name: str
    category: Optional[str]
    stock_quantity: int
    purchase_price: float
    selling_price: float
    stock_value: float
    description: Optional[str] = None
    
    class config:
        orm_mode = True 

class InventorySummary(BaseModel):
    total_products: int 
    total_stock_quantity: int
    total_inventory_value: float

    