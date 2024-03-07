from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    id:int = Field(..., gt=0, description="User ID must be greater than zero")
    name:str = Field(..., min_length=1, max_length=100, description="User name must be between 1 and 100 characters")
    email:EmailStr