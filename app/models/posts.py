# models/posts.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from database.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Post(Base):

    __tablename__ = "posts"

    # post_id
    id = Column(Integer, primary_key=True,index=True)

    # user_id
    user_id = Column(Integer,ForeignKey("users.id"),index=True,nullable=False)

    # post title
    title = Column(String(150),nullable=False)
    # post content 
    content = Column(Text,nullable=False)
    # post created_at
    created_at = Column(DateTime, default=func.now(),index=True,nullable=False)
    # post updated_at
    updated_at = Column(DateTime,default=func.now(),onupdate=func.now(),nullable=False)
    
    # ORM relationship
    # post = query(Post).first()
    # post.user.username
    
    user = relationship("User", back_populates="posts") 

    # post.likes

    likes = relationship("Like",
                         foreign_keys="Like.post_id",
                         back_populates="post"
                        )
    # post.views 
    views = relationship("PostView",
                         foreign_keys="PostView.post_id",
                         back_populates="post")
   
    # post.comments
    comments = relationship("Comment",
                            back_populates="post")
    
    def __repr__(self):
        return f"<Post id = {self.id} Title = {self.title}>"
    