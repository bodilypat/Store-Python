#app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchema.exc import SQLAlchemyError

from app.core.config import settings

#----------------------------------------------------------------
# Base Model
#----------------------------------------------------------------
class Base(DeclarativeBase):
    pass

#----------------------------------------------------------------
# Engine Configuration
#----------------------------------------------------------------
engine = create_engine(
    settings.get_database_url,
    echo=settings.DEBUG,                  # Log SQL queries in development
    pool_pre_ping=True,                   # Check connections healthy
    pool_size=10,                         # Default pool size
    max_overflow=20,                      # Extra connections beyond pool size
)

#----------------------------------------------------------------
# Session Factory
#----------------------------------------------------------------
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)
#----------------------------------------------------------------
# Dependency for FastAPI
#----------------------------------------------------------------
def get_db():
    """
    FastAPI dependency that provides a database session.
    and ensures it is properly closed.
    """
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        raise
    finally:
        db.close()

        
