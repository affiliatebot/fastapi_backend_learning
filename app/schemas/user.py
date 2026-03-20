from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True