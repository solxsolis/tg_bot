from keyboards.cm_panel_keyboard_back_to_main_menu import cm_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.cm_panel.create_post.create_post import FSM_create_post_cm
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
from bd_handlers.create_post.create_post import create_post
from bd_handlers.create_post.check_user_name import check_db_user_name
import datetime

config = dotenv_values(CONFIG_DIR / '.env')

@dp.message_handler(state=FSM_create_post_cm.post_link)
async def post_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_link'] = message.text
        await state.finish()
        
        user_id = int(message.from_user.id)
        post_name = str(data['post_name'])
        post_disc = str(data['post_disc'])
        post_tag = str(data['post_tag'])
        post_link = str(data['post_link'])
        curr_date = str(datetime.datetime.now().date())
        curr_time = str(datetime.datetime.now().time().replace(microsecond=0))
        user_name = await check_db_user_name(user_id=user_id)

        await create_post(post_name=post_name, post_disc=post_disc, post_tag=post_tag, post_link=post_link, user_name=user_name, create_data=curr_date, create_time=curr_time)

        await bot.send_message(chat_id=message.from_user.id, text=f"User ID: {message.from_user.id}\n" f"Post name: {post_name}\n" f"Post description: {post_disc}\n"f"Post tags: #{post_tag}\n"f"Post link: {post_link}\n" f"Author: {user_name}\n" f"Date: {curr_date}\n" f"Time: {curr_time}\n", reply_markup=cm_panel_keyboard_back_to_main_menu)
        await bot.send_message(chat_id=message.from_user.id, text=f"<b>Name:</b>\n<i>{post_name}</i>\n"f"\n<b>Description:</b>\n<i>{post_disc}</i>\n"f"\n<b>Link:</b>\n<i>{post_link}</i>\n"f"\n<b>Tag:</b>\n<i>#{post_tag}</i>\n", parse_mode = 'HTML')
