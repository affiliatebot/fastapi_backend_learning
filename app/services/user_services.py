# service/user_service.py
from fastapi import HTTPException
import logging
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserInput
from core.security import hash_password

logger = logging.getLogger(__name__)

def normalize(value: str) -> str:
    return value.lower().strip()

def create_new_user(db: Session, user: UserInput):

    username = normalize(user.username)
    email = normalize(user.email)

    try:
        db_user = User(
            username=username,
            email=email,
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
