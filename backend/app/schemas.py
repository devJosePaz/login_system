from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(UserCreate):
    id: int
    
    class Config:
        from_attributes = True
