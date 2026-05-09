# service/user_service.py
from fastapi import HTTPException
import logging
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.users import User
from models.posts import Post
from schemas.user import UserInputSchema, UserLoginSchema
from core.security import hash_password, verify_password
from core.jwt_token import create_token

logger = logging.getLogger(__name__)

# def normalize(value: str) -> str:
#     return value.lower().strip() 

def create_user(user: UserInputSchema,db: Session):

    # username = normalize(user.username)
    # email = normalize(user.email)

    try:
        db_user = User(
            username=user.username,
            email=user.email,
            password_hash=hash_password(user.password)
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        logger.info(f"User created: id={db_user.id}, email={db_user.email}")

        return db_user

    except IntegrityError as e:
        db.rollback()

        logger.warning(f"Integrity error: {str(e)}")

        # DB-level duplicate handling
        raise HTTPException(
            status_code=400,
            detail="Username or Email already exists"
        )

    except Exception as e:
        db.rollback()

        logger.error(f"Unexpected error: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )


# login function
def login(credentials:UserLoginSchema,db:Session):
    
    # fetch user data from db
    db_user = (
                db.query(User)
               .filter(User.email == credentials.email).first()
               )
    if db_user == None:
        raise Exception("Invalid credentials")
    
    # verify password
    if not verify_password(plain_password=credentials.password,
                           hash_password=db_user.password_hash):
        
        raise Exception("Invalid credentials")
    
    # generate token with user_id,expiry
    payload = {"user_id":db_user.id}
    token = create_token(payload)
    
    return {
            "access_token": token,
            "token_type": "bearer"
            }
