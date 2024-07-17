from keyboards.cm_panel_keyboard_back_to_main_menu import cm_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSM_change_post_cm(StatesGroup):
    post_id = State()
    post_name = State()
    post_disc = State()
    post_tag = State()
    post_link = State()

@dp.callback_query_handler(text='change_post_cm')
async def cm_panel_change_post_callback(callback_query: types.CallbackQuery):
    await FSM_change_post_cm.post_id.set()
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id, text=f"Enter post ID(key): ", reply_markup=cm_panel_keyboard_back_to_main_menu)