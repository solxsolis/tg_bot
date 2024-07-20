from aiogram import types

user_keyboard_main_menu = types.InlineKeyboardMarkup()
ap_btn_rl = types.InlineKeyboardButton('Get referral link', callback_data='get_ref_link')
ap_btn_vp = types.InlineKeyboardButton('View posts', callback_data='view_posts')
ap_btn_sv = types.InlineKeyboardButton('Send voice message', callback_data = 'send_voice')
user_keyboard_main_menu.row(ap_btn_vp, ap_btn_sv)
user_keyboard_main_menu.row(ap_btn_rl)