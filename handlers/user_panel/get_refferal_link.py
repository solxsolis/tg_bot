from aiogram import types
from config.bot_config import dp, bot
from keyboards.user_panel_keyboard_back_to_main_menu import user_keyboard_back_to_main_menu


@dp.callback_query_handler(text='get_ref_link')
async def user_panel_view_posts_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id, text=f'your referral link will be here', reply_markup=user_keyboard_back_to_main_menu)

