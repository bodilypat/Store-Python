#app/models/product.py

from sqlalchemy import Column, Integer, String, Float, DECIMAL, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.db.session import Base

class Product(Base):
    __tablename__ = 'products'
    
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'), ondelete='SET NULL')
    barcode = Column(String(50), unique=True)
    purchase_price = Column(DECIMAL(10, 2), nullable=False)
    selling_price = Column(DECIMAL(10, 2), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    description = Column(String(255))
    
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    
    # Relationships
    category = relationship('Category', back_populates='products', passive_deletes=True)
    purchase_items = relationship('PurchaseItem', back_populates='product', cascade='all, delete-orphan')
    sale_items = relationship('SaleItem', back_populates='product', cascade='all, delete-orphan')