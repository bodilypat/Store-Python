#app/services/sale_service.py (with stack reduction and error handling)
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.product import Product
from app.schemas.sale import SaleCreate, SaleItemCreate

class SaleService:
    @staticmethod
    def create_sale(db: Session, sale_data: SaleCreate):
        try:
            # Create the sale record
            new_sale = Sale(
                customer_id=sale_data.customer_id,
                total_amount=0  # Will be updated after adding items
            )
            db.add(new_sale)
            db.commit()
            db.refresh(new_sale)

            total_amount = 0

            # Add sale items
            for item in sale_data.items:
                product = db.query(Product).filter(Product.product_id == item.product_id).first()
                if not product:
                    raise HTTPException(status_code=404, detail=f"Product with ID {item.product_id} not found")

                sale_item = SaleItem(
                    sale_id=new_sale.sale_id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    unit_price=product.price
                )
                db.add(sale_item)
                total_amount += item.quantity * product.price

            # Update total amount for the sale
            new_sale.total_amount = total_amount
            db.commit()
            db.refresh(new_sale)

            return new_sale
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        
    @staticmethod
    def get_sale(db: Session, sale_id: int):
        sale = db.query(Sale).filter(Sale.sale_id == sale_id).first()
        if not sale:
            raise HTTPException(status_code=404, detail="Sale not found")
        return sale
    
    @staticmethod
    def list_sales(db: Session):
        return db.query(Sale).all()
    
    @staticmethod
    def delete_sale(db: Session, sale_id: int):
        sale = db.query(Sale).filter(Sale.sale_id == sale_id).first()
        if not sale:
            raise HTTPException(status_code=404, detail="Sale not found")
        db.delete(sale)
        db.commit()

    
    