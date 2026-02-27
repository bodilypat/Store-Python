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
    
    @staticmethod
    def combined_dashboard(db: Session):

        today = datetime.today()

        #-----------------------------------------
        # Sales Summary
        #-----------------------------------------
        total_sales = db.query(Sale).filter(func.extract('month', Sale.sale_date) == today.month, func.extract('year', Sale.sale_date) == today.year).count()
        total_revenue = db.query(func.sum(Sale.total_amount)).filter(func.extract('month', Sale.sale_date) == today.month, func.extract('year', Sale.sale_date) == today.year).scalar() or 0.0
        total_profit = db.query(func.sum((SaleItem.unit_price - Product.purchase_price) * SaleItem.quantity)).join(Sale).join(Product).filter(func.extract('month', Sale.sale_date) == today.month, func.extract('year', Sale.sale_date) == today.year).scalar() or 0.0
        sales_summary = {
            "total_sales": total_sales,
            "total_revenue": total_revenue,
            "total_profit": total_profit
        }
        #-----------------------------------------
        # Today's Revenue
        #-----------------------------------------
        today_revenue = db.query(func.sum(Sale.total_amount)).filter(func.date(Sale.sale_date) == today.date()).scalar() or 0.0

        #-----------------------------------------
        # Low Stock Count (<= 5)        
        #-----------------------------------------
        low_stock_count = db.query(Product).filter(Product.stock_quantity <= 5).count()

        return {
            "sales_summary": sales_summary,
            "today_revenue": today_revenue,
            "low_stock_count": low_stock_count
        }
    
        #-----------------------------------------
        # Top Selling Products
        #-----------------------------------------
        top_products = (
            db.query(
                Product.product_name,
                func.sum(SaleItem.quantity).label('total_quantity'),
                func.sum(SaleItem.unit_price * SaleItem.quantity).label('total_revenue')
            )
            .join(SaleItem, Product.product_id == SaleItem.product_id)
            .group_by(Product.product_id)
            .order_by(func.sum(SaleItem.quantity).desc())
            .limit(5)
            .all()
        )

        return {
            "sales_summary": sales_summary,
            "today_revenue": today_revenue,
            "low_stock_count": low_stock_count,
            "top_products": top_products
        }
    


    
