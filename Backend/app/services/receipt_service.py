#app/services/receipt_service.py
from sqlalchemy.orm import Session
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.product import Product
from datetime import datetime

class ReceiptService:
    @staticmethod
    def generate_receipt(db: Session, sale_id: int):
        # Fetch the sale and related items
        sale = db.query(Sale).filter(Sale.sale_id == sale_id).first()
        if not sale:
            raise ValueError("Sale not found")

        items = (
            db.query(SaleItem, Product)
            .join(Product, SaleItem.product_id == Product.product_id)
            .filter(SaleItem.sale_id == sale_id)
            .all()
        )
        # Generate receipt content
        receipt_items = []
        subtotal = 0
        for sale_item, product in items:
            total_price = sale_item.quantity * sale_item.unit_price
            subtotal += total_price
            receipt_items.append({
                "product_name": product.product_name,
                "quantity": sale_item.quantity,
                "unit_price": float(sale_item.unit_price),
                "total_price": total_price
            })

        tax_rate = 0.07  # Example tax rate
        tax_amount = subtotal * tax_rate
        total_amount = subtotal + tax_amount

        receipt_data = {
            "sale_id": sale.sale_id,
            "customer_id": sale.customer_id,
            "sale_date": sale.sale_date.strftime("%Y-%m-%d %H:%M:%S"),
            "items": receipt_items,
            "subtotal": subtotal,
            "tax_amount": tax_amount,
            "total_amount": total_amount
        }
        return receipt_data
