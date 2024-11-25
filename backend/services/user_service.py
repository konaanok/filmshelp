from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from auth_utils import get_password_hash, verify_password
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate

class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)

    async def register_user(self, user: UserCreate) -> str:
        hashed_password = get_password_hash(user.password)
        await self.user_repository.create_user(user, hashed_password)
        
        return "User registered successfully"
    
    async def authenticate_user(self, email: str, password: str) -> Optional[dict]:
        user = await self.user_repository.get_user_by_email(email)
        if not user:
            return None
        if verify_password(password, user["hashed_password"]):
            return {"id": user["id"], "email": user["email"]}
        return None
    
