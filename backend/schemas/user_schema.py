from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class Token(BaseModel): 
    access_token: str 
    token_type: str 

class LoginRequest(BaseModel):
    email: str
    password: str

class MessageResponse(BaseModel):
    message: str
