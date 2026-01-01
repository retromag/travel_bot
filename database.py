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

async def tour_request_save(user_id: int, username: str,country: str, region: str | None, stars: str,
    food: str, nights: int, adults : int, children: int, children_age: str | None, dates: str, place: str,
    budget: str):
    async with db_pool.acquire() as connection:
        await connection.execute(
            """
            INSERT INTO tour_request (user_id, username, country, region, stars, food, nights, adults,
            children, children_age, dates, place, budget)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)
            """,
            user_id, username, country,
            region, stars, food, nights,
            adults, children, children_age,
            dates, place, budget
        )
