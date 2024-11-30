import asyncpg
async def get_database_connection():
    return await asyncpg.connect(
        host='localhost',
        port=5432,
        user='postgres',
        password='12345',
        database='postgres'
)