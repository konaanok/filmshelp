from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import insert, select
from models.user_model import user_table
from schemas.user_schema import UserCreate
from database.db_connection import get_database_connection


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
        
    async def get_user_by_email(self, email: str) -> Optional[dict]:
        conn = await get_database_connection()
        try:
            query = 'SELECT * FROM "user" WHERE "email" = $1'
            user_record = await conn.fetchrow(query, email)
            return dict(user_record) if user_record else None
        finally:
            await conn.close()
    
    async def get_user_id_by_username(self, username: str) -> Optional[int]:
        query = select(user_table.c.id).where(user_table.c.username == username)
        result = await self.db.execute(query)
        user = result.fetchone()
        return user.id if user else None
