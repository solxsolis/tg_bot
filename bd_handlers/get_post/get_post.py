import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values

config = dotenv_values(CONFIG_DIR / '.env')

USER = config['user']
PWD = config['password']
DB = config['database']
HOST = config['host']

async def get_posts():
    conn = await asyncpg.connect(user=USER, password=PWD, database=DB, host=HOST)
    rows = await conn.fetch('SELECT * FROM posts ORDER BY key ASC')
    await conn.close()
    if not rows:
        return 'None'
    else:
        return rows