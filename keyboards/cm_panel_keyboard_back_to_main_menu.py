from aiogram import types

cm_panel_keyboard_back_to_main_menu = types.InlineKeyboardMarkup()
ap_btn_mm = types.InlineKeyboardButton('Back to main menu', callback_data='main_menu_cm')
cm_panel_keyboard_back_to_main_menu.row(ap_btn_mm)