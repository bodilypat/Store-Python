#app/services/auth_service.py   Auth service
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models import User, UserRole
from app.schemas.auth import UserCreate
from app.core.security import hash_password, verify_password, create_access_token

class AuthService:
    @staticmethod
    def register_user(db: Session, user_data: UserCreate) -> User:
        existing_user = db.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        
        hashed_password = hash_password(user_data.password)
        new_user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=hashed_password,
            role=UserRole.CASHIER
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> User:
        user = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return user
    
    @staticmethod
    def create_token(user: User) -> str:
        return create_access_token(data={"user_id": user.user_id, "role": user.role.value})
    

    
