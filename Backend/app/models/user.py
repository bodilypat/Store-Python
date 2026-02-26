# app/models/user.py  Full SQLAlchemy User model 
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.db.session import Base
import enum

class UserRole(enum.Enum):
    admin = 'admin'
    cashier = 'cashier'

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.cashier)
    phone_number = Column(String(20), nullable=True)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    
    # Relationships
    sales = relationship("Sale", back_populates="user")
    