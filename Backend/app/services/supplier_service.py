#app/services/supplier_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.supplier_repo import SupplierRepository
from app.schemas.supplier import SupplierCreate, SupplierUpdate

class SupplierService:
    @staticmethod
    def create_supplier(db: Session, supplier_in: SupplierCreate):
        if SupplierRepository.get_supplier_by_email(db, supplier_in.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        return SupplierRepository.create_supplier(db, supplier_in)
    
    @staticmethod
    def update_supplier(db: Session, supplier_id: int, updated: SupplierUpdate):
        supplier = SupplierRepository.get_supplier_by_id(db, supplier_id)
        if not supplier:
            raise HTTPException(status_code=404, detail="Supplier not found")
        if updated.email and SupplierRepository.get_supplier_by_email(db, updated.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        return SupplierRepository.update_supplier(db, supplier_id, updated)
    
    @staticmethod
    def delete_supplier(db: Session, supplier_id: int):
        supplier = SupplierRepository.get_supplier_by_id(db, supplier_id)
        if not supplier:
            raise HTTPException(status_code=404, detail="Supplier not found")
        return SupplierRepository.delete_supplier(db, supplier_id)
    
    @staticmethod
    def get_supplier(db: Session, supplier_id: int):
        supplier = SupplierRepository.get_supplier_by_id(db, supplier_id)
        if not supplier:
            raise HTTPException(status_code=404, detail="Supplier not found")
        return supplier
    
    @staticmethod
    def list_suppliers(db: Session, skip: int = 0, limit: int = 100):
        return SupplierRepository.list_suppliers(db, skip, limit)
    
    
    
