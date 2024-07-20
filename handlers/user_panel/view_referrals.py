from aiogram import types
from config.bot_config import dp, bot
from keyboards.user_panel_keyboard_back_to_main_menu import user_keyboard_back_to_main_menu
from bd_handlers.referral.get_referrals import get_referrals

@dp.callback_query_handler(text='view_refs')
async def user_panel_view_refs_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    ref_id = callback_query.from_user.id
    refs = await get_referrals(ref_id)
    if not refs:
        await bot.send_message(chat_id=callback_query.from_user.id, text = f"You don't have any referrals yet", reply_markup=user_keyboard_back_to_main_menu)
    else:
        message = ''
        for ref in refs:
            message += f"{ref['user_id']}\n"
        await bot.send_message(chat_id=callback_query.from_user.id, text=message, reply_markup=user_keyboard_back_to_main_menu)
        

