from pydantic import BaseModel, EmailStr

# Incoming registration
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Incoming login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Outgoing user info
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

# JWT Token response
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
