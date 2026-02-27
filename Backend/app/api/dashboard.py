#app/api/dashboard.py
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.dashboard import SalesSummary, TopProduct, MonthlyRevenue, CashierPerformance, CombinedDashboardResponse
from app.services.dashboard_service import DashboardService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/combined", response_model=CombinedDashboardResponse)
def get_combined_dashboard(
    start_date: str = Query(None, description="Start date in YYYY-MM-DD format"),
    end_date: str = Query(None, description="End date in YYYY-MM-DD format"),
    limit: int = Query(5, description="Number of top products to return"),
    year: int = Query(..., description="Year for which to calculate monthly revenue"),
    db: Session = Depends(get_db)
):
    service = DashboardService(db)
    combined_data = service.get_combined_dashboard_data(start_date, end_date, limit, year)
    return combined_data

@router.get("/summary")
def sales_summary(
    start_date: str = Query(None, description="Start date in YYYY-MM-DD format"),
    end_date: str = Query(None, description="End date in YYYY-MM-DD format"),
    db: Session = Depends(get_db)
):
    service = DashboardService(db)
    summary = service.get_sales_summary(start_date, end_date)
    return summary

@router.get("/top-products")
def top_selling_products(
    limit: int = Query(5, description="Number of top products to return"),
    db: Session = Depends(get_db)
):
    service = DashboardService(db)
    top_products = service.get_top_selling_products(limit)
    return top_products

@router.get("/monthly-revenue")
def monthly_revenue(
    year: int = Query(..., description="Year for which to calculate monthly revenue"),
    db: Session = Depends(get_db)
):
    service = DashboardService(db)
    revenue_data = service.get_monthly_revenue(year)
    return revenue_data

@router.get("/cashier-performance")
def cashier_performance(
    db: Session = Depends(get_db)
):
    service = DashboardService(db)
    performance_data = service.get_cashier_performance()
    return performance_data

