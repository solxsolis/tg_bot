import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
import key

config = dotenv_values(CONFIG_DIR / '.env')

user = str(config['user'])
password = str(config['password'])
database = str(config['database'])
host = str(config['host'])

async def create_cm(user_id, user_name):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    current_key = await key.get_key_role()+1
    await conn.execute('''INSERT INTO role(key, user_id, user_role, user_name) VALUES($1, $2, $3, $4)''', current_key, user_id, 'cm', user_name)
    await conn.close()