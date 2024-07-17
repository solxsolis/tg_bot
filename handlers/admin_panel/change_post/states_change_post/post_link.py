from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.get_post import FSM_change_post
from bd_handlers.change_post.change_post import change_post
from bd_handlers.create_post.check_user_name import check_db_user_name
import datetime

@dp.message_handler(state=FSM_change_post.post_link)
async def post_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_link'] = str(message.text)

        post_name = str(data['post_name'])
        post_disc = str(data['post_disc'])
        post_tag = str(data['post_tag'])
        post_link = str(data['post_link'])
        post_id = str(data['key'])
        user_id = int(message.from_user.id)
        curr_date = str(datetime.datetime.now().date())
        curr_time = str(datetime.datetime.now().time().replace(microsecond=0))

        await state.finish()
        user_name = await check_db_user_name(user_id=user_id)
        await change_post(post_name=post_name, post_disc=post_disc, post_tag=post_tag, post_link=post_link, change_user_name = user_name, change_date=curr_date, change_time = curr_time, post_id=post_id)
        await bot.send_message(chat_id=message.from_user.id, text=f"Post ID: {post_id}\n" f"Post name: {post_name}\n" f"Post description: {post_disc}\n" f"Post tags: {post_tag}\n" f"New link: {post_link}\n" f"Post changes successfully\n", reply_markup=admin_panel_keyboard_back_to_main_menu)
        