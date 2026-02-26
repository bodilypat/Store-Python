#app/models/sale.py
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.db.session import Base

class Sale(Base):
    __tablename__ = 'sales'

    sale_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id', ondelete='SET NULL'), nullable=True)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    sale_date = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

# Relationships
    customer = relationship("Customer", back_populates="sales")
    sale_items = relationship("SaleItem", back_populates="sale", cascade="all, delete-orphan")

    