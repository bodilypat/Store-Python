#app/services/purchase_service.py  (with stock increase)
from sqlalchemy.orm import Session  
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.models.purchase import Purchase 
from app.models.purchase_item import PurchaseItem
from app.models.product import Product
from app.schemas.purchase import PurchaseCreate

class PurchaseService:
    @staticmethod
    def create_purchase(db: Session, purchase_data: PurchaseCreate) -> Purchase:
        try:
            # Create the purchase record
            new_purchase = Purchase(
                supplier_id=purchase_data.supplier_id,
                user_id=purchase_data.user_id,
                purchase_date=purchase_data.purchase_date,
                total_amount=purchase_data.total_amount
            )
            db.add(new_purchase)
            db.commit()
            db.refresh(new_purchase)

            # Create purchase items and update stock
            for item in purchase_data.items:
                purchase_item = PurchaseItem(
                    purchase_id=new_purchase.purchase_id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    unit_price=item.unit_price
                )
                db.add(purchase_item)

                # Update product stock
                product = db.query(Product).filter(Product.product_id == item.product_id).first()
                if product:
                    product.stock_quantity += item.quantity  # Increase stock for purchases
                    db.add(product)

            db.commit()
            return new_purchase

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        
    @staticmethod
    def get_purchase(db: Session, purchase_id: int) -> Purchase:
        purchase = db.query(Purchase).filter(Purchase.purchase_id == purchase_id).first()
        if not purchase:
            raise HTTPException(status_code=404, detail="Purchase not found")
        return purchase
    
    @staticmethod
    def list_purchases(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Purchase).offset(skip).limit(limit).all()   
    
    @staticmethod
    def delete_purchase(db: Session, purchase_id: int):
        purchase = db.query(Purchase).filter(Purchase.purchase_id == purchase_id).first()
        if not purchase:
            raise HTTPException(status_code=404, detail="Purchase not found")
        db.delete(purchase)
        db.commit()

    @staticmethod
    def update_purchase(db: Session, purchase_id: int, purchase_data: PurchaseCreate):
        purchase = db.query(Purchase).filter(Purchase.purchase_id == purchase_id).first()
        if not purchase:
            raise HTTPException(status_code=404, detail="Purchase not found")

        try:
            # Update purchase details
            purchase.supplier_id = purchase_data.supplier_id
            purchase.user_id = purchase_data.user_id
            purchase.purchase_date = purchase_data.purchase_date
            purchase.total_amount = purchase_data.total_amount
            db.add(purchase)

            # Update purchase items and stock
            existing_items = {item.product_id: item for item in db.query(PurchaseItem).filter(PurchaseItem.purchase_id == purchase_id).all()}
            for item in purchase_data.items:
                if item.product_id in existing_items:
                    # Update existing item
                    existing_item = existing_items[item.product_id]
                    stock_change = item.quantity - existing_item.quantity  # Calculate stock change
                    existing_item.quantity = item.quantity
                    existing_item.unit_price = item.unit_price
                    db.add(existing_item)
                else:
                    # Add new item
                    new_item = PurchaseItem(
                        purchase_id=purchase_id,
                        product_id=item.product_id,
                        quantity=item.quantity,
                        unit_price=item.unit_price
                    )
                    db.add(new_item)
                    stock_change = item.quantity  # New stock addition

                # Update product stock
                product = db.query(Product).filter(Product.product_id == item.product_id).first()
                if product:
                    product.stock_quantity += stock_change  # Adjust stock based on change
                    db.add(product)

            db.commit()
            return purchase

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
            
    