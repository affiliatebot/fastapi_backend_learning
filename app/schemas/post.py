from pydantic import BaseModel, Field
from datetime import datetime


# output schema to get all posts
class PostsResponse(BaseModel):

    id:int
    title:str
    content:str
    created_at:datetime

    class Config:
        from_attributes=True

# input schema to create post
class CreatePostRequest(BaseModel):

    title: str = Field(
        min_length=3,
        max_length=100
    )# to not allow empty or blank spaces only

    content:str = Field(
        min_length=1,
        max_length=5000
    )# to not allow empty or blank spaces only and giant content

# output schema to create post
class CreatePostResponse(BaseModel):

    id:int # post_id
    title:str
    content:str
    created_at:datetime

    class Config:
        from_attributes=True
##################################################################

# Input schema to edit a post
class EditPostRequest(BaseModel):
    
    
    title:str | None = None
    content:str | None = None

# output schema to edit a post
class EditPostResponse(BaseModel):
    
    id:int
    title:str
    content:str
    updated_at:datetime

###################################################################
    
class DeletePostResponse(BaseModel):

    message:str