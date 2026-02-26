#app/models/category.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.session import Base

class Category(Base):
    __tablename__ = 'categories'
    
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    
    # relationships
    products = relationship('Product', back_populates='category')
