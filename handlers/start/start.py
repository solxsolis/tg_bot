from aiogram import types
from config.bot_config import dp, bot
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from keyboards.cm_panel_keyboard_main_menu import cm_keyboard_main_menu
from bd_handlers.role.check_user_role import check_db_user_role
from bd_handlers.get_post.get_post import get_posts
from keyboards.user_panel_create import user_keyboard_create
from keyboards.user_panel_keyboard_main_menu import user_keyboard_main_menu
from bd_handlers.referral.add_user import add_user

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    referred_by = None

    if message.get_args():
        try:
            referred_by = int(message.get_args())
            if referred_by == user_id:
                await message.reply("You cannot refer yourself")
                return
        except ValueError:
            referred_by = None

    await add_user(user_id, referred_by)

    check_user_role = await check_db_user_role(user_id=user_id)
    if check_user_role=='admin':
        await bot.send_message(chat_id=message.from_user.id, text=f"Your ID: {message.from_user.id}", reply_markup=admin_panel_keyboard_main_menu)
    elif check_user_role == 'cm':
        await bot.send_message(chat_id=message.from_user.id, text=f"Your ID: {message.from_user.id}", reply_markup=cm_keyboard_main_menu)
    elif check_user_role == 'user':
        await bot.send_message(chat_id=message.from_user.id, text=f"If you want to try making a test payment: \nCard number: 1111 1111 1111 1026\n12/22\nCVC: 000", reply_markup=user_keyboard_main_menu)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=f'Welcome', reply_markup=user_keyboard_create)
        

