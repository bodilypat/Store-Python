#app/services/inventory_service.py
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.product import Product
from app.models.category import Category
from app.models.sale_item import SaleItem
from app.models.purchase_item import PurchaseItem

class InventoryService:
    @staticmethod
    def get_full_inventory(db: Session):
        products = (
            db.query(
                Product.product_id,
                Product.product_name,
                Product.description,
                Product.price,
                Product.stock_quantity,
                Category.category_name,
                func.coalesce(func.sum(SaleItem.quantity), 0).label('total_sold'),
                func.coalesce(func.sum(PurchaseItem.quantity), 0).label('total_purchased')
            )
            .join(Category, Product.category_id == Category.category_id)
            .outerjoin(SaleItem, Product.product_id == SaleItem.product_id)
            .outerjoin(PurchaseItem, Product.product_id == PurchaseItem.product_id)
            .group_by(Product.product_id, Category.category_name)
        )
        results = []
        for product in products:
            results.append({
                "product_id": product.product_id,
                "product_name": product.product_name,
                "description": product.description,
                "price": float(product.price),
                "stock_quantity": product.stock_quantity,
                "category_name": product.category_name,
                "total_sold": int(product.total_sold),
                "total_purchased": int(product.total_purchased)
            })
        return results
    
    @staticmethod
    def get_low_stock(db: Session, threshold: int = 5):
        low_stock_products = (
            db.query(Product)
            .filter(Product.stock_quantity < threshold)
            .all()
        )
        return low_stock_products
    
    @staticmethod
    def get_inventory_summary(db: Session):
        total_products = db.query(func.count(Product.product_id)).scalar()
        total_categories = db.query(func.count(Category.category_id)).scalar()
        total_stock_value = db.query(func.sum(Product.price * Product.stock_quantity)).scalar() or 0
        return {
            "total_products": total_products,
            "total_categories": total_categories,
            "total_stock_value": float(total_stock_value)
        }
    
    @staticmethod
    def get_stock_movements(db: Session, product_id: int):
        sales = (
            db.query(SaleItem)
            .filter(SaleItem.product_id == product_id)
            .all()
        )
        purchases = (
            db.query(PurchaseItem)
            .filter(PurchaseItem.product_id == product_id)
            .all()
        )
        return {
            "sales": sales,
            "purchases": purchases
        }
    
    