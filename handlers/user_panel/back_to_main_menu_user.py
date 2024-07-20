from aiogram import types
from config.bot_config import dp, bot
from keyboards.user_panel_keyboard_main_menu import user_keyboard_main_menu


@dp.callback_query_handler(text='main_menu_user', state='*')
async def admin_panel_main_menu_callback(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text=f"If you want to try making a test payment: \nCard number: 1111 1111 1111 1026\n12/22\nCVC: 000", reply_markup=user_keyboard_main_menu)
