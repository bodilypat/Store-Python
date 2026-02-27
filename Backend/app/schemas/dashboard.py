#app/schemas/dashboard_schema.py 
from pydantic import BaseModel
from typing import List

class SalesSummary(BaseModel):
    total_sales: float
    total_revenue: float
    total_profit: float
    
class TopProduct(BaseModel):
    product_id: int
    product_name: str
    total_quantity_sold: int
    total_revenue: float

class MonthlyRevenue(BaseModel):
    month: str
    total_revenue: float

class CashierPerformance(BaseModel):
    user_id: int
    cashier_name: str
    total_sales: int
    total_revenue: float