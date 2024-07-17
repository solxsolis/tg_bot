from aiogram import types

user_keyboard_create = types.InlineKeyboardMarkup()
ap_btn_ca = types.InlineKeyboardButton('Create an account', callback_data='create_user')
user_keyboard_create.row(ap_btn_ca)
