#app/services/dashboard_service.py
from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from datetime import datetime
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.product import Product
from app.models.user import User

class DashboardService:
    @staticmethod
    def sales_summary(db: Session, start_date=None, end_date=None):
        query = db.query(Sale)
        if start_date and end_date:
            query = query.filter(Sale.sale_date.between(start_date, end_date))

        total_sales = query.count()
        total_revenue = db.query(func.sum(Sale.total_amount)).filter(Sale.sale_date.between(start_date, end_date)).scalar() or 0.0
        total_quantity_sold = db.query(func.sum(SaleItem.quantity)).join(Sale).filter(Sale.sale_date.between(start_date, end_date)).scalar() or 0   

        # Profit = (selling - purchasing) * quantity
        profit_query = db.query(
            func.sum((SaleItem.unit_price - Product.purchase_price) * SaleItem.quantity)
                ).join(Sale).join(Product).filter(Sale.sale_date.between(start_date, end_date))
        total_profit = profit_query.scalar() or 0.0
        return {
            "total_sales": total_sales,
            "total_quantity_sold": total_quantity_sold,
            "total_revenue": total_revenue,
            "total_profit": total_profit
        }
    
    @staticmethod
    def top_selling_products(db: Session, limit=5):
        results = (
            db.query(
                Product.product_name,
                func.sum(SaleItem.quantity).label('total_quantity'),
                func.sum(SaleItem.unit_price * SaleItem.quantity).label('total_revenue')
            )
            .join(SaleItem, Product.product_id == SaleItem.product_id)
            .group_by(Product.product_id)
            .order_by(func.sum(SaleItem.quantity).desc())
            .limit(limit)
            .all()
        )
        return results
    
    @staticmethod
    def monthly_revenue(db: Session, year: int):
        results = (
            db.query(
                extract('month', Sale.sale_date).label('month'),
                func.sum(Sale.total_amount).label('total_revenue')
            )
            .filter(extract('year', Sale.sale_date) == year)
            .group_by(extract('month', Sale.sale_date))
            .order_by(extract('month', Sale.sale_date))
            .all()
        )
        return results
    
    @staticmethod
    def cashier_performance(db: Session, start_date=None, end_date=None):
        query = db.query(
            User.user_id,
            User.full_name.label('cashier_name'),
            func.count(Sale.sale_id).label('total_sales'),
            func.sum(Sale.total_amount).label('total_revenue')
        ).join(Sale, User.user_id == Sale.customer_id)  # Assuming user_id is linked to sales
        if start_date and end_date:
            query = query.filter(Sale.sale_date.between(start_date, end_date))
        results = query.group_by(User.user_id).order_by(func.sum(Sale.total_amount).desc()).all()
        return results
    

    
    