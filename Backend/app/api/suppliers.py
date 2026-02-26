#app/api/suppliers.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.supplier import SupplierCreate, SupplierUpdate, SupplierRead
from app.services.supplier_service import SupplierService

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

@router.post("/", response_model=SupplierRead)
def create_supplier(supplier_in: SupplierCreate, db: Session = Depends(get_db)):
    return SupplierService.create_supplier(db, supplier_in)

@router.get("/{supplier_id}", response_model=SupplierRead)
def list_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = SupplierService.get_supplier(db, supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier

@router.put("/{supplier_id}", response_model=SupplierRead)
def update_supplier(supplier_id: int, supplier_in: SupplierUpdate, db: Session = Depends(get_db)):
    supplier = SupplierService.update_supplier(db, supplier_id, supplier_in)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier

@router.delete("/{supplier_id}", response_model=SupplierRead)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = SupplierService.delete_supplier(db, supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier

