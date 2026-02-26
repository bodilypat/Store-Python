#app/models/purchase.py
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, TIMESTAMP, text 
from sqlalchemy.orm import relationship
from app.db.session import Base

class Purchase(Base):
    __tablename__ = 'purchases'

    purchase_id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id', ondelete='SET NULL'))
    purchase_date = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    total_amount = Column(DECIMAL(10, 2), nullable=False)

    # Relationships
    supplier = relationship("Supplier", back_populates="purchases")
    purchase_items = relationship("PurchaseItem", back_populates="purchase", cascade="all, delete-orphan")
