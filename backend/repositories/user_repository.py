from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import insert, select
from models.user_model import user_table
from schemas.user_schema import UserCreate


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: UserCreate, hashed_password: str):
        stmt = insert(user_table).values(
            email=user.email,
            username=user.username,
            hashed_password=hashed_password
        )
        try:
            await self.db.execute(stmt)
            await self.db.commit()
        except IntegrityError:
            await self.db.rollback()
            raise ValueError("User with this email already exists")

