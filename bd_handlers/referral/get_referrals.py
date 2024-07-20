import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
import key

config = dotenv_values(CONFIG_DIR / '.env')

user = str(config['user'])
password = str(config['password'])
database = str(config['database'])
host = str(config['host'])

async def get_referrals(referrer_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    refs = await conn.fetch('''SELECT user_id FROM refferal WHERE referrer_id=$1''', referrer_id)
    await conn.close()
    if not refs:
        return None
    else:
        return refs