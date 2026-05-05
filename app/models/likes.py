# models/likes.py
from sqlalchemy import Column, Integer,DateTime, ForeignKey, UniqueConstraint
from database.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Like(Base):

    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,ForeignKey("users.id"),index=True,nullable=False)
    post_id = Column(Integer,ForeignKey("posts.id"),index=True,nullable=False)

    created_at = Column(DateTime,default=func.now(),nullable=False)

    # rule to prevent duplicate likes
    __table_args__ = (
        UniqueConstraint("user_id", "post_id", name="unique_like"),
    )

    # orm relationships

    # like.user
    user = relationship("User",
                        foreign_keys=[user_id],
                        back_populates="likes")
    # like.post
    post = relationship("Post",
                         foreign_keys=[post_id],
                         back_populates="likes")
    
    
    
    