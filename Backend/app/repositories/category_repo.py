#app/repositories/category_repo.py
from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate

class CategoryRepository:
    @staticmethod
    def get_by_id(db: Session, category_id: int) -> Category:
        return db.query(Category).filter(Category.category_id == category_id).first()
    
    @staticmethod
    def get_by_name(db: Session, name: str) -> Category:
        return db.query(Category).filter(Category.category_name == name).first()
    
    @staticmethod
    def create(db: Session, category: CategoryCreate) -> Category:
        db_category = Category(category_name=category.category_name)
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    
    @staticmethod
    def update(db: Session, db_category: Category, category_update: CategoryUpdate) -> Category:
        db_category.category_name = category_update.category_name
        db.commit()
        db.refresh(db_category)
        return db_category
    
    @staticmethod
    def delete(db: Session, db_category: Category) -> None:
        db.delete(db_category)
        db.commit()

    @staticmethod
    def list(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Category).offset(skip).limit(limit).all()
    
    