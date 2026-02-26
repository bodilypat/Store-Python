#app/api/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.db.session import get_db
from app.repositories.user_repo import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if UserRepository(db).get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserRepository(db).create_user(user)

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserRepository(db).get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = UserRepository(db).get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserRepository(db).update_user(db_user, user)

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserRepository(db).get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    UserRepository(db).delete_user(db_user)

@router.get("/", response_model=list[UserRead])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return UserRepository(db).list_users(skip=skip, limit=limit)


