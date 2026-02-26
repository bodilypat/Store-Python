#app/core/security.py
from datetime import datetime, timedelta
from typing import Optional, Any, Union

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings

#------------------------------------------------------
# Password Hashing (bcrypt)
#------------------------------------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash a plaintext password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plaintext password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)

#------------------------------------------------------
# JWT Token Handling
#------------------------------------------------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def create_access_token(
        subject: Union[str, Any],
        expire_delta: Optional[timedelta] = None,
        ) -> str:
        """
           Create a JWT access token for a given subject and expiration delta.
        """
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {
             "sub": str(subject),
             "exp": expire,
             "iat": datetime.utcnow(),
        }
        encoded_jwt = jwt.encode(
            to_encode, 
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )
        return encoded_jwt
def decode_access_token(token: str) -> Optional[dict]:
    """Decode a JWT access token and return the payload if valid."""
    try:
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )   
    
#----------------------------------------------------------------------
# Dependency: Get Current User ID
#----------------------------------------------------------------------
def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    """Extract the user ID from the JWT token."""
    payload = decode_access_token(token)
    user_id: str = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return int(user_id)

#----------------------------------------------------------------------
# Optional: Role-Based Access Control (RBAC) Dependency
#----------------------------------------------------------------------
def require_role(required_role: str):
    """Dependency to enforce role-based access control."""
    def role_checker(token: str = Depends(oauth2_scheme)) -> str:
        payload = decode_access_token(token)
        role = payload.get("role")
        if role is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return role
    return role_checker
