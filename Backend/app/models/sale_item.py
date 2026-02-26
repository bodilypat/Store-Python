#app/models/sale_item.py 

from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db.session import Base

class SaleItem(Base):
    __tablename__ = 'sale_items'
    
    sale_item_id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey('sales.sale_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id', ondelete='SET NULL'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)

    # Relationships
    sale = relationship("Sale", back_populates="sale_items")
    product = relationship("Product", back_populates="sale_items")
    