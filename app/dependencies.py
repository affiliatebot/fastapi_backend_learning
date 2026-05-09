from database.db import SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi import HTTPException
from core.jwt_token import verify_token
from models.users import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token:str = Depends(oauth_scheme),
                     db:Session = Depends(get_db)):

    # verify token expiry
    # verify token tampering and return user_id
    user_id = verify_token(token)

    user = (db.query(User)
            .filter(User.id == user_id)).first()
    
    if user is None:
        raise HTTPException(status_code=401,
                            detail="User not found")
    
    
    return user


def require_admin(current_user:User=Depends(get_current_user)):
    
    if current_user.role != "admin":
        raise HTTPException(status_code=403,
                            detail="Admin only")
    return current_user