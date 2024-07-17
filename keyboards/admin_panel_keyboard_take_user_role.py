from aiogram import types

admin_panel_keyboard_take_user_role=types.InlineKeyboardMarkup()

ap_btn_tura = types.InlineKeyboardButton('Admin', callback_data='take_user_role_admin')
ap_btn_turcm = types.InlineKeyboardButton('Content manager', callback_data='take_user_role_cm')
admin_panel_keyboard_take_user_role.row(ap_btn_tura, ap_btn_turcm)
