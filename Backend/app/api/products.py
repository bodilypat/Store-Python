#app/api/product/products.py     api router
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductRead
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductRead)
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create_product(db, product_in)

@router.get("/{product_id}", response_model=ProductRead)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = ProductService.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductRead)
def update_product(product_id: int, product_in: ProductUpdate, db: Session = Depends(get_db)):
    product = ProductService.update_product(db, product_id, product_in)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    success = ProductService.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully"}

@router.get("/", response_model=list[ProductRead])
def list_products(db: Session = Depends(get_db), limit: int = 100, skip: int = 0):
    return ProductService.list_products(db, limit=limit, skip=skip)


