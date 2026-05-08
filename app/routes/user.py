from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.user import UserInputSchema, UserOutputSchema, UserLoginSchema, TokenResponseSchema
from models.user import User
from services.user_services import create_user , login

router = APIRouter()




## create user api
@router.post("/users", response_model=UserOutputSchema, status_code=status.HTTP_201_CREATED)
def create_user_api(user: UserInputSchema, db: Session = Depends(get_db)):
    
    return create_user(user=user, db=db)

## login api
@router.post("/login",response_model=TokenResponseSchema)
def login_api(credentials:UserLoginSchema, db:Session = Depends(get_db)):
    
    return login(credentials=credentials,db=db)
    

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()