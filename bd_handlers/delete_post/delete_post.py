import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values

config = dotenv_values(CONFIG_DIR / '.env')

user = str(config['user'])
password = str(config['password'])
daatbase = str(config['database'])
host = str(config['host'])

async def delete_post(post_id):
    conn = await asyncpg.connect(user=user, password=password, database=daatbase, host=host)
    await conn.execute('''DELETE FROM posts WHERE key=$1''', post_id)
    await conn.close()