#app/models/purchase_item.py

from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db.session import Base

class PurchaseItem(Base):
    __tablename__ = 'purchase_items'
    
    purchase_item_id = Column(Integer, primary_key=True)
    purchase_id = Column(Integer, ForeignKey('purchases.purchase_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id', ondelete='SET NULL'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)

    # Relationships
    purchase = relationship("Purchase", back_populates="purchase_items")
    product = relationship("Product", back_populates="purchase_items")
    