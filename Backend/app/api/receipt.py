#app/api/receipt.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.receipt_service import ReceiptService

router = APIRouter(prefix="/receipts", tags=["Receipts"])

@router.get("/{sale_id}")
def get_receipt(sale_id: int, db: Session = Depends(get_db)):
    receipt_data = ReceiptService.generate_receipt(db, sale_id)
    if not receipt_data:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt_data

@router.get("/pdf/{sale_id}")
def get_receipt_pdf(sale_id: int, db: Session = Depends(get_db)):
    pdf_data = ReceiptService.generate_receipt_pdf(db, sale_id)
    if not pdf_data:
        raise HTTPException(status_code=404, detail="Receipt PDF not found")
    text_receipt = ReceiptService.generate_receipt(db, sale_id)
    if text_receipt:
        print("Text Receipt:")
        print(text_receipt) 
    return {"pdf_data": pdf_data, "text_receipt": text_receipt}



