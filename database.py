
import sqlite3 as sql

async def sql_connecter():
    con = sql.connect("youtube_bot.db")
    cur = con.cursor()
    return con, cur


async def create_tables():
    con, cur = await sql_connecter()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id BIGINT,
            username VARCHAR(50)
        )""")
    


async def add_user(user_id: int, username: str):
    con, cur = await sql_connecter()

    user = cur.execute(f"SELECT * FROM users WHERE user_id = {user_id}").fetchone()
    if not user:
        cur.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
        con.commit()
