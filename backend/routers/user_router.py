from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter
from database.database import get_user_db
from schemas import LoginRequest, MessageResponse, Token, UserCreate
from services import UserService
from auth_utils import create_access_token

auth_router = APIRouter()

@auth_router.post("/register", response_model=MessageResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_user_db)):
    user_service = UserService(db)
    try:
        message = await user_service.register_user(user)
        return {"message": message}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
 
@auth_router.post("/login", response_model=Token)
async def login(form_data: LoginRequest, db: AsyncSession = Depends(get_user_db)):
    user_service = UserService(db)
    user = await user_service.authenticate_user(form_data.email, form_data.password)
    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "cookie"}

