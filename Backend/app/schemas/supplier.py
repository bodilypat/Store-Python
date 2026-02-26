#app/schemas/supplier.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class SupplierCreate(BaseModel):
    company_name: str
    contact_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

class SupplierUpdate(BaseModel):
    company_name: Optional[str] = None
    contact_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

class Supplier(BaseModel):
    supplier_id: int
    company_name: str
    contact_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

    class Config:
        orm_mode = True

        