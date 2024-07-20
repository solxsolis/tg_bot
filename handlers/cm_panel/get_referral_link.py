from aiogram import types
from config.bot_config import dp, bot
from keyboards.cm_panel_keyboard_back_to_main_menu import cm_panel_keyboard_back_to_main_menu

def create_referral_link(user_id):
    return f"https://t.me/sfgfd_echo_bot?start={user_id}"

@dp.callback_query_handler(text='get_ref_link_cm')
async def user_panel_get_link_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    user_id = callback_query.from_user.id
    ref_link = create_referral_link(user_id)
    await bot.send_message(chat_id=callback_query.from_user.id, text=f"Your referral link: {ref_link}", reply_markup=cm_panel_keyboard_back_to_main_menu)
