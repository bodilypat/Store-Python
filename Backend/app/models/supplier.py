#app/models/supplier.py
from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from app.db.session import Base

class Supplier(Base):
    __tablename__ = 'suppliers'

    supplier_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(100), nullable=False)
    contact_name = Column(String(100))
    email = Column(String(255), unique=True)
    phone_number = Column(String(20))
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    # Optional: Add relationships to purchases if needed
    # purchases = relationship("Purchase", back_populates="supplier")
    

