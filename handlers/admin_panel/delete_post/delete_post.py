from aiogram import types
from config.bot_config import dp, bot
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSM_delete_post(StatesGroup):
    post_id = State()

@dp.callback_query_handler(text='delete_post_admin')
async def admin_panel_delete_post_callback(callback_query: types.CallbackQuery):
    await FSM_delete_post.post_id.set()
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id, text=f"Enter post ID: ", reply_markup=admin_panel_keyboard_back_to_main_menu)

    