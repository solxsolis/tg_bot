import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values

config = dotenv_values(CONFIG_DIR / '.env')

USER = config['user']
PWD = config['password']
DB = config['database']
HOST = config['host']

async def check_db_user_role(user_id):
    conn = await asyncpg.connect(user=USER, password=PWD, database=DB, host=HOST)
    row = await conn.fetchrow('SELECT user_role FROM role WHERE user_id = $1', user_id)
    await conn.close()
    if not row:
        return 'None'
    else:
        return row['user_role']