import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
import key

config = dotenv_values(CONFIG_DIR / '.env')

user = str(config['user'])
password = str(config['password'])
database = str(config['database'])
host = str(config['host'])

async def add_user(user_id, referrer_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    flag = await conn.fetch('''SELECT * FROM refferal WHERE user_id=$1''', user_id)
    if not flag:
        await conn.execute('''INSERT INTO refferal(user_id, referrer_id) VALUES($1, $2)''',user_id, referrer_id)
    await conn.close()