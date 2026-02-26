#app/repositories/supplier_repo.py
from sqlalchemy.orm import Session
from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate, SupplierUpdate

class SupplierRepository:
    @staticmethod
    def create_supplier(db: Session, supplier: SupplierCreate) -> Supplier:
        db_supplier = Supplier(**supplier.dict())
        db.add(db_supplier)
        db.commit()
        db.refresh(db_supplier)
        return db_supplier
    
    @staticmethod
    def get_supplier(db: Session, supplier_id: int) -> Supplier:
        return db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
    
    @staticmethod
    def get_suppliers(db: Session, skip: int = 0, limit: int = 100) -> list[Supplier]:
        return db.query(Supplier).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_supplier(db: Session, supplier_id: int, supplier_update: SupplierUpdate) -> Supplier:
        db_supplier = db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
        if not db_supplier:
            return None
        for key, value in supplier_update.dict(exclude_unset=True).items():
            setattr(db_supplier, key, value)
        db.commit()
        db.refresh(db_supplier)
        return db_supplier
    
    @staticmethod
    def delete_supplier(db: Session, supplier_id: int) -> bool:
        db_supplier = db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
        if not db_supplier:
            return False
        db.delete(db_supplier)
        db.commit()
        return True
    