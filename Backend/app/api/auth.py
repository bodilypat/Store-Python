# app/api/auth.py  Auth router
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.db.session import get_db
from app.schemas.auth import UserCreate, UserRead, Token
from app.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model= UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    new_user = auth_service.register_user(user)
    return JSONResponse(content={"message": "User registered successfully", "user": UserRead.from_orm(new_user).dict()})

@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    token = auth_service.authenticate_user(user.username, user.password)
    if token:
        return Token(access_token=token, token_type="bearer")
    return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)

@router.post("/logout")
def logout():
    # Implement logout logic (e.g., token invalidation)
    return JSONResponse(content={"message": "User logged out successfully"})

@router.post("/refresh", response_model=Token)
def refresh_token():
    # Implement token refresh logic
    return JSONResponse(content={"message": "Token refreshed successfully", "access_token": "new_token", "token_type": "bearer"})   

@router.get("/me", response_model=UserRead)
def get_current_user(db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    current_user = auth_service.get_current_user()
    if current_user:
        return UserRead.from_orm(current_user)
    return JSONResponse(content={"message": "User not authenticated"}, status_code=401)

@router.post("/change-password")
def change_password(new_password: str, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    success = auth_service.change_password(new_password)
    if success:
        return JSONResponse(content={"message": "Password changed successfully"})
    return JSONResponse(content={"message": "Failed to change password"}, status_code=400)

@router.post("/reset-password")
def reset_password(email: str, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    success = auth_service.reset_password(email)
    if success:
        return JSONResponse(content={"message": "Password reset email sent"})
    return JSONResponse(content={"message": "Failed to send password reset email"}, status_code=400)

@router.post("/verify-email")
def verify_email(token: str, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    success = auth_service.verify_email(token)
    if success:
        return JSONResponse(content={"message": "Email verified successfully"})
    return JSONResponse(content={"message": "Failed to verify email"}, status_code=400)

@router.post("/resend-verification")
def resend_verification_email(email: str, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    success = auth_service.resend_verification_email(email)
    if success:
        return JSONResponse(content={"message": "Verification email resent successfully"})
    return JSONResponse(content={"message": "Failed to resend verification email"}, status_code=400)

@router.post("/deactivate")
def deactivate_account(db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    success = auth_service.deactivate_account()
    if success:
        return JSONResponse(content={"message": "Account deactivated successfully"})
    return JSONResponse(content={"message": "Failed to deactivate account"}, status_code=400)


