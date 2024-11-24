import asyncpg
from sqlalchemy.ext.asyncio import AsyncSession
from auth_utils import get_password_hash, verify_password
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_database_connection():
    return await asyncpg.connect(
        host='localhost',
        port=5432,
        user='postgres',
        password='12345',
        database='postgres'
)

async def authenticate_user(email: str, password: str):
    conn = await get_database_connection()
    query = 'SELECT * FROM "user" WHERE "email" = $1'
    user_record = await conn.fetchrow(query, email)
    await conn.close()
    if user_record and verify_password(password, user_record["hashed_password"]):
        return {"email": user_record["email"]}
    return None

class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)

    async def register_user(self, user: UserCreate) -> str:
        hashed_password = get_password_hash(user.password)
        await self.user_repository.create_user(user, hashed_password)
        
        return "User registered successfully"
    