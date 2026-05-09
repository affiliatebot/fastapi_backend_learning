# models/post_view.py
from sqlalchemy import Column, Integer,DateTime, ForeignKey, UniqueConstraint
from database.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class View(Base):
    # post view table
    __tablename__ = "views"

    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,ForeignKey("users.id"),index=True,nullable=False)
    post_id = Column(Integer,ForeignKey("posts.id"),index=True,nullable=False)
    # event table
    # rows == views
    created_at = Column(DateTime,default=func.now(),nullable=False)

    # orm relationships
    
    # view.user

    user = relationship("User",
                        foreign_keys=[user_id],
                        back_populates="views")
    
    # view.post
    post = relationship("Post",
                        foreign_keys=[post_id],
                        back_populates="views")
 