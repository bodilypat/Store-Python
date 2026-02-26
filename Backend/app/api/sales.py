#app/api/sales.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.sale import SaleCreate, SaleResponse
from app.services.sale_service import SaleService

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    try:
        sale_service = SaleService(db)
        new_sale = sale_service.create_sale(sale)
        return new_sale
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{sale_id}", response_model=SaleResponse)
def get_sale(sale_id: int, db: Session = Depends(get_db)):
    try:
        sale_service = SaleService(db)
        sale = sale_service.get_sale(sale_id)
        if not sale:
            raise HTTPException(status_code=404, detail="Sale not found")
        return sale
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/", response_model=List[SaleResponse])
def list_sales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        sale_service = SaleService(db)
        sales = sale_service.list_sales(skip=skip, limit=limit)
        return sales
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{sale_id}")
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    try:
        sale_service = SaleService(db)
        success = sale_service.delete_sale(sale_id)
        if not success:
            raise HTTPException(status_code=404, detail="Sale not found")
        return {"detail": "Sale deleted successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
