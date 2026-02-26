#app/services/product_service.py
from sqlalchemy.orm import Session
from app.repositories.product_repo import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate

class ProductService:
    @staticmethod
    def create_product(db: Session, product_in: ProductCreate):
        return ProductRepository.create(db, product_in)
    
    @staticmethod
    def get_product(db: Session, product_id: int):
        product = ProductRepository.get_by_id(db, product_id)
        if not product:
            raise Exception("Product not found")
        return product
    
    @staticmethod
    def update_product(db: Session, product_id: int, product_in: ProductUpdate):
        product = ProductRepository.get_by_id(db, product_id)
        if not product:
            raise Exception("Product not found")
        return ProductRepository.update(db, product, product_in)
    
    @staticmethod
    def delete_product(db: Session, product_id: int):
        product = ProductRepository.get_by_id(db, product_id)
        if not product:
            raise Exception("Product not found")
        return ProductRepository.delete(db, product)
    
    @staticmethod
    def list_products(db: Session, skip: int = 0, limit: int = 100):
        return ProductRepository.list(db, skip=skip, limit=limit)
    
    
    
    