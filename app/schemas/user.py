from pydantic import BaseModel, EmailStr, Field , field_validator

class UserInputSchema(BaseModel):

    username: str = Field(min_length=3, max_length=30) 
    email:EmailStr
    password:str = Field(min_length=8 , max_length=128)

    # custom validation for password field
    @field_validator(password)
    def validate_password(cls, value):
        
        if " " in value:
            raise ValueError("Password must not contain spaces")
        
        
        return value 


class UserOutputSchema(BaseModel):
    id:int
    username:str
    email:EmailStr

    class Config:
        from_attributes=True

###############################################
# login Input schema
class UserLoginSchema(BaseModel):

    email:EmailStr # format,datatype,required validation
    password:str = Field(
        min_length=8,
        max_length=128
    )

# Login Output Schema
class TokenResponseSchema(BaseModel):

    access_token: str
    token_type: str