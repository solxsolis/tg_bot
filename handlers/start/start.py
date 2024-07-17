from aiogram import types
from config.bot_config import dp, bot
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from keyboards.cm_panel_keyboard_main_menu import cm_keyboard_main_menu
from bd_handlers.role.check_user_role import check_db_user_role
from bd_handlers.get_post.get_post import get_posts
from keyboards.user_panel_create import user_keyboard_create
import logging
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    check_user_role = await check_db_user_role(user_id=user_id)
    if check_user_role=='admin':
        await bot.send_message(chat_id=message.from_user.id, text=f"Your ID: {message.from_user.id}", reply_markup=admin_panel_keyboard_main_menu)
    elif check_user_role == 'cm':
        await bot.send_message(chat_id=message.from_user.id, text=f"Your ID: {message.from_user.id}", reply_markup=cm_keyboard_main_menu)
    elif check_user_role == 'user':
        rows = await get_posts()
        posts = []
        for x in rows:
            post = x
            post_id = post['key']
            post_name = post['post_name']
            get_post = f'Post ID: {post_id}\nPost name: {post_name}'
            posts.append(get_post)
        num_posts = len(posts)
        if num_posts == 0:
            await bot.send_message(chat_id=message.from_user.id, text=f'No posts\n')
        else:
            for post in posts:
                await bot.send_message(chat_id=message.from_user.id, text=f'\n{post}\n')

    else:
        logging.info(f"welcome message sent")
        await bot.send_message(chat_id=message.from_user.id, text=f'Welcome', reply_markup=user_keyboard_create)
        

