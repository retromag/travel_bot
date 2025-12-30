import asyncpg
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

db_pool = None

async def connect_db():
    global db_pool
    db_pool = await asyncpg.create_pool(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

async def save_consultation(user_id: int, username: str, question: str):
    async with db_pool.acquire() as connection:
        await connection.execute(
            """
            INSERT INTO consultations (user_id, username, question)
            VALUES ($1, $2, $3)
            """,
            user_id,
            username,
            question
        )
