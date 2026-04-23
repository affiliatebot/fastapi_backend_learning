from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.user import UserInput, UserOutput
from models.user import User
from services.user_services import create_new_user

router = APIRouter()




@router.post("/users", response_model=UserOutput, status_code=status.HTTP_201_CREATED)
def create_user(user: UserInput, db: Session = Depends(get_db)):
    
    return create_new_user(db,user)


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()