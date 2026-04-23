# models/user.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database.db import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,index=True)
    username = Column(String(50),index=True,unique=True,nullable=False)
    email = Column(String(100),index=True,unique=True,nullable=False)
    password_hash = Column(String(255),index=False,unique=False,nullable=False)
    # Sets time only on creation
    created_at = Column(DateTime,default=func.now(),nullable=False)
    # Sets time on creation and refreshes on every update
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(),nullable=False)
    # Account status
    is_active = Column(Boolean, default=True,nullable=False)
    is_verified = Column(Boolean, default=False,nullable=False)


    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"