#app/repositories/user_repo.py
from sqlalchemy.orm import Session
from app.models.user import User, UserRole
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password

class UserRepository:
    """
    Handles all database operations for User model.
    Methods:
    - create_user: Creates a new user in the database.
    - get_user_by_email: Retrieves a user by their email.
    - get_user_by_id: Retrieves a user by their ID.
    - update_user: Updates user details.    
    - delete_user: Deletes a user from the database.
    """
    @staticmethod
    def create_user(db: Session, user_create: UserCreate) -> User:
        hashed_password = hash_password(user_create.password)
        db_user = User(
            full_name=user_create.full_name,
            email=user_create.email,
            password_hash=hashed_password,
            role=user_create.role
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User:
        return db.query(User).filter(User.user_id == user_id).first()
    @staticmethod
    def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User:
        db_user = db.query(User).filter(User.user_id == user_id).first()
        if not db_user:
            return None
        if user_update.full_name is not None:
            db_user.full_name = user_update.full_name
        if user_update.email is not None:
            db_user.email = user_update.email
        if user_update.password is not None:
            db_user.password_hash = hash_password(user_update.password)
        if user_update.role is not None:
            db_user.role = user_update.role
        db.commit()
        db.refresh(db_user)
        return db_user
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        db_user = db.query(User).filter(User.user_id == user_id).first()
        if not db_user:
            return False
        db.delete(db_user)
        db.commit()
        return True
    
    


