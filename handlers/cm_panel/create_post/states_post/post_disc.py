from keyboards.cm_panel_keyboard_back_to_main_menu import cm_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.cm_panel.create_post.create_post import FSM_create_post_cm

@dp.message_handler(state=FSM_create_post_cm.post_disc)
async def post_disc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_disc'] = message.text
        await FSM_create_post_cm.next()
        await bot.send_message(chat_id=message.from_user.id, text=f"User ID: {message.from_user.id}\n" f"Post name: {data['post_name']}\n" f"Post description: {data['post_disc']}\n"f"Enter tags: ", reply_markup=cm_panel_keyboard_back_to_main_menu)
        