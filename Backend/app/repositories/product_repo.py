#app/repositories/product_repo.py
from sqlalchemy import session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

class ProductRepository:
    @staticmethod
    def get_by_id(db: session, product_id: int) -> Product | None:
        return db.query(Product).filter(Product.product_id == product_id).first()
    
    @staticmethod
    def get_by_barcode(db: session, barcode: str) -> Product | None:
        return db.query(Product).filter(Product.barcode == barcode).first()
    
    @staticmethod
    def create(db: session, product_data: ProductCreate) -> Product:
        new_product = Product(**product_data.dict())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    
    @staticmethod
    def update(db: session, product: Product, update_data: ProductUpdate) -> Product:
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(product, field, value)
        db.commit()
        db.refresh(product)
        return product
    
    @staticmethod
    def delete(db: session, product: Product) -> None:
        db.delete(product)
        db.commit()

    @staticmethod
    def list(db: session, skip: int = 0, limit: int = 100) -> list[Product]:
        return db.query(Product).offset(skip).limit(limit).all()
    
    