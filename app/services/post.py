from fastapi import HTTPException
import logging
#from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.users import User
from models.posts import Post
from schemas.post import *


logger = logging.getLogger(__name__)

# create a post
def create_post(post:CreatePostRequest,user:User, db:Session):
    
    

    db_post = Post(title=post.title,
                content=post.content,
                user_id=user.id)
    
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post

# edit a post
def edit_post(id:int, post:EditPostRequest ,user:User, db:Session):

    db_post = db.query(Post).filter(Post.id == id).first()

    # ownership authorization
    if db_post.user_id != user.id:
        raise HTTPException(status_code=403,
                            detail="you are not owner")

    if post.title is not None:
        db_post.title = post.title
    
    if post.content is not None:
        db_post.content = post.content

    db.commit()
    db.refresh(db_post)

    return db_post

# delete a post
def delete_post(id:int,user:User,db:Session):
    # fetch the post
    db_post = db.query(Post).filter(Post.id == id).first()
    # post existence check
    # backend can't trust frontend state
    if db_post is None:
        raise HTTPException(status_code=404,
                            detail="Post not found")
    # check ownership
    if db_post.user_id != user.id:
        raise HTTPException(status_code=403,
                            detail="cannot delete another user's post")
    try:
        # delete row
        db.delete(db_post)
        # commit so no rollback
        db.commit()
        return {"message":"Post deleted successfully"}
    
    # to catch db error like IntegrityError
    except Exception: 
        #if db.commit() fail X then rollback the transaction
        db.rollback()
        # to again raise same error
        raise

    

# get all post with pagination and sorted
def get_posts(user:User, db:Session,limit:int, offset:int):
    
    posts = (db.query(Post)
             .filter(Post.user_id == user.id)
             .order_by(Post.created_at.desc())
             .offset(offset)
             .limit(limit)
             .all())
    
    return posts