#app/api/inventory.py
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.inventory_service import InventoryService

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.get("/")
def full_inventory(db: Session = Depends(get_db)):
    service = InventoryService(db)
    return service.get_full_inventory()

@router.get("/low-stock")
def low_stock_inventory(threshold: int = Query(10, gt=0), db: Session = Depends(get_db)):
    service = InventoryService(db)
    return service.get_low_stock(threshold)   

@router.get("/out-of-stock")
def out_of_stock_inventory(db: Session = Depends(get_db)):
    service = InventoryService(db)
    return service.get_out_of_stock()

@router.get("/search")
def search_inventory(query: str, db: Session = Depends(get_db)):
    service = InventoryService(db)
    return service.search_inventory(query)

@router.get("/summary")
def inventory_summary(db: Session = Depends(get_db)):
    service = InventoryService(db)
    return service.get_inventory_summary()

@router.get("/movements")
def inventory_movements(db: Session = Depends(get_db)):
    service = InventoryService(db)
    return service.get_inventory_movements()

