from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user
from schemas.post import *
from models.users import User
from services.post import get_posts, create_post ,edit_post

router = APIRouter()


# create a post
@router.post("/posts",response_model=CreatePostOutputSchema,
                      status_code=201) # 201 -> created successfully
def create_post_api(post:CreatePostInputSchema,
                    user:User=Depends(get_current_user),
                    db:Session=Depends(get_db)):
    
    return create_post(post=post,user=user,db=db)

# edit a post
@router.patch("/posts/{id}", response_model=EditPostResponse)
def edit_post_api(id:int,
                  post:EditPostRequest,
                  user:User = Depends(get_current_user),
                  db:Session = Depends(get_db)):
    
    return edit_post(id=id,
                     post=post,
                     user=user,
                     db=db)


# get all posts 
@router.get("/posts", response_model=[PostOutputSchema])
def get_post_api(limit:int=10,
                 offset:int=0,
                 user:User=Depends(get_current_user),
                 db:Session=Depends(get_db)
                 ):

    return get_posts(user=user,db=db,limit=limit,offset=offset)
    