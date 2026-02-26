#app/services/category_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.category_repo import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate

class CategoryService:
    @staticmethod
    def create_category(db: Session, category_in: CategoryCreate):
        if CategoryRepository.get_by_name(db, category_in.category_name):
            raise HTTPException(status_code=400, detail="Category with this name already exists")
        return CategoryRepository.create(db, category_in)
    
    @staticmethod
    def get_category(db: Session, category_id: int):
        category = CategoryRepository.get(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category
    
    @staticmethod
    def update_category(db: Session, category_id: int, updates: CategoryUpdate):
        category = CategoryRepository.get(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        if updates.category_name and CategoryRepository.get_by_name(db, updates.category_name):
            raise HTTPException(status_code=400, detail="Category with this name already exists")
        return CategoryRepository.update(db, category_id, updates)
    
    @staticmethod
    def delete_category(db: Session, category_id: int):
        category = CategoryRepository.get(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return CategoryRepository.delete(db, category_id)
    
    @staticmethod
    def list_categories(db: Session):
        return CategoryRepository.list(db)
    
    