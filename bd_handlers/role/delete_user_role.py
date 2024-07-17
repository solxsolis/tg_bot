import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values

config = dotenv_values(CONFIG_DIR / '.env')

user = str(config['user'])
password = str(config['password'])
database = str(config['database'])
host = str(config['host'])

async def delete_user_role(user_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''DELETE FROM role WHERE user_id=$1''', user_id)
    await conn.close()