import asyncio
import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
config = dotenv_values(CONFIG_DIR / '.env')

user = str(config['user'])
password = str(config['password'])
database = str(config['database'])
host = str(config['host'])


async def get_key_role():
    try:
        conn = await asyncpg.connect(
            user=user,
            password=password,
            database=database,
            host=host
        )
        
        row = await conn.fetchrow("SELECT * FROM role ORDER BY key DESC LIMIT 1")
        
        if row:
            first_value = row[0]
            return first_value
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await conn.close()

async def get_key_post():
    try:
        conn = await asyncpg.connect(
            user=user,
            password=password,
            database=database,
            host=host
        )
        
        row = await conn.fetchrow("SELECT * FROM posts ORDER BY key DESC LIMIT 1")
        
        if row:
            first_value = row[0]
            return first_value
        else:
            return -1
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await conn.close()
#if __name__ == '__main__':
#    current_key = asyncio.run(get_first_value()) + 1