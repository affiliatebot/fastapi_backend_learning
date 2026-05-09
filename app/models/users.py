# models/user.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean ,Enum
from database.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

class UserRole(enum.Enum):

    user = "user"
    admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,index=True)
    username = Column(String(50),index=True,unique=True,nullable=False)
    email = Column(String(100),index=True,unique=True,nullable=False)
    password_hash = Column(String(255),index=False,unique=False,nullable=False)
    # role (user , admin)
    role = Column(Enum(UserRole),default=UserRole.user,nullable=False)

    # Sets time only on creation
    created_at = Column(DateTime,default=func.now(),nullable=False)
    # Sets time on creation and refreshes on every update
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(),nullable=False)
    # Account status
    is_active = Column(Boolean, default=True,nullable=False)
    is_verified = Column(Boolean, default=False,nullable=False)
    # soft delete
    is_deleted = Column(Boolean,default=False,nullable=False)
    # role
    role = Column(String(20),default="user",nullable=False)

    # orm relationship
    posts = relationship("Post",back_populates="user")

    # user table <-> subscription table
    followers = relationship("Subscriber",
                             foreign_keys="Subscriber.creator_id",
                             back_populates="creator") 
    
    # user table <-> subscription table
    following = relationship("Subscriber",
                             foreign_keys="Subscriber.subscriber_id",
                             back_populates="subscriber") 
    # user.likes
    likes = relationship("Like",
                         foreign_keys="Like.user_id",
                         back_populates="user")
    # user.postviews
    views = relationship("PostView",
                         foreign_keys="PostView.user_id",
                         back_populates="user")
    # user.comments
    comments = relationship("Comment", 
                            back_populates="user")
    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"