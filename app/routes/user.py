from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import User as UserSchema
from app.models.user import User
from app.database.db import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = User(name=user.name, age=user.age)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()