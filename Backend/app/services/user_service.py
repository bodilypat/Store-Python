#app/services/user_service.py 
from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate, UserUpdate

class UserService:
    @staticmethod
    def create_user(db: Session, user_create: UserCreate):
        return UserRepository.create_user(db, user_create)
    @staticmethod
    def get_user(db: Session, user_id: int):
        return UserRepository.get_user(db, user_id)
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return UserRepository.get_user_by_email(db, email)
    @staticmethod
    def update_user(db: Session, user_id: int, user_update: UserUpdate):
        return UserRepository.update_user(db, user_id, user_update)
    @staticmethod
    def delete_user(db: Session, user_id: int):
        return UserRepository.delete_user(db, user_id)
    
    