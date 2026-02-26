#app/api/categories.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryOut
from app.services.category_service import CategoryService   

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryOut)
def create_category(category_in: CategoryCreate, db: Session = Depends(get_db)):
    return CategoryService.create_category(db, category_in)

@router.get("/{category_id}", response_model=CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = CategoryService.get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, category_in: CategoryUpdate, db: Session = Depends(get_db)):
    category = CategoryService.update_category(db, category_id, category_in)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    success = CategoryService.delete_category(db, category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return None


