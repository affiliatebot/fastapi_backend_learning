from pydantic import BaseModel, EmailStr

class UserInput(BaseModel):
    username: str
    email:EmailStr
    password:str

class UserOutput(BaseModel):
    id:int
    username:str
    email:EmailStr

    class Config:
        from_attributes=True