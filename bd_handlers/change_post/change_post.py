import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values

config = dotenv_values(CONFIG_DIR / '.env')

USER = config['user']
PWD = config['password']
DB = config['database']
HOST = config['host']

async def change_post(post_name, post_disc, post_tag, post_link, change_user_name, change_date, change_time, post_id):
    conn = await asyncpg.connect(user=USER, password=PWD, database=DB, host=HOST)
    await conn.execute('UPDATE posts SET post_name=$1, post_disc=$2, post_tag=$3, post_link=$4, change_user=$5, change_date=$6, change_time=$7 WHERE key=$8', post_name, post_disc, post_tag, post_link, change_user_name, change_date, change_time, int(post_id))
    await conn.close()
