import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
import key

config = dotenv_values(CONFIG_DIR / '.env')

USER = config['user']
PWD = config['password']
DB = config['database']
HOST = config['host']

async def create_post(post_name, post_disc, post_tag, post_link, user_name, create_data, create_time):
    conn = await asyncpg.connect(user=USER, password=PWD, database=DB, host=HOST)
    current_key = await key.get_key_post()+1
    await conn.execute('''INSERT INTO posts(key, post_name, post_disc, post_tag, post_link, user_name, create_data, create_time) VALUES($1, $2, $3, $4, $5, $6, $7, $8)''',current_key, post_name, post_disc, post_tag, post_link, user_name, create_data, create_time)
    await conn.close()