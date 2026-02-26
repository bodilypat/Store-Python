#app/core/dependencies.py
from typing import Generator
from sqlalchemy.orm import Session
from .db.session import SessionLocal

def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that provides a SQLAlchemy session
    and ensures proper commit/rollback handling.
    Yields:
        Session: A SQLAlchemy database session.
    """

    db: Session = SessionLocal()
    try:
        yield db
        db.commit()  # Commit transaction if no exceptions occur
    except Exception as e:
        db.rollback()  # Rollback transaction on error
        raise e  # Re-raise the exception for FastAPI to handle
    finally:
        db.close()  # Ensure the session is closed after use

        