#app/api/purchases.py 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.purchase import PurchaseCreate, PurchaseResponse
from app.services.purchase_service import PurchaseService

router = APIRouter(prefix="/purchases", tags=["Purchases"])

@router.post("/", response_model=PurchaseResponse)
def create_purchase(purchase: PurchaseCreate, db: Session = Depends(get_db)):
    try:
        purchase_service = PurchaseService(db)
        return purchase_service.create_purchase(purchase)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{purchase_id}", response_model=PurchaseResponse)
def get_purchase(purchase_id: int, db: Session = Depends(get_db)):
    try:
        purchase_service = PurchaseService(db)
        return purchase_service.get_purchase(purchase_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/", response_model=list[PurchaseResponse])
def list_purchases(db: Session = Depends(get_db)):
    try:
        purchase_service = PurchaseService(db)
        return purchase_service.list_purchases()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{purchase_id}")
def delete_purchase(purchase_id: int, db: Session = Depends(get_db)):
    try:
        purchase_service = PurchaseService(db)
        purchase_service.delete_purchase(purchase_id)
        return {"detail": "Purchase deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    