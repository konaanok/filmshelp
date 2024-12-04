from typing import Optional
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from auth_utils import get_password_hash, verify_password
from repositories import UserRepository
from schemas import UserCreate, MessageResponse

class UserService:
    __instance: Optional['UserService'] = None
    user_repository: Optional[UserRepository] = None

    def __new__(cls, db: AsyncSession = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db: AsyncSession = None):
        if not hasattr(self, "_initialized") or not self._initialized:
            self.user_repository = UserRepository(db)
            self._initialized = True

    async def register_user(self, user: UserCreate) -> MessageResponse:
        hashed_password = get_password_hash(user.password)
        await self.user_repository.create_user(user, hashed_password)
        
        return MessageResponse(message="User registered successfully")
    
    async def authenticate_user(self, email: str, password: str) -> Optional[dict]:
        user = await self.user_repository.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Cookie"},
            )
        if verify_password(password, user["hashed_password"]):
            return MessageResponse(message="User authenticated successfully")
        return None
    