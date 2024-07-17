from aiogram import types

admin_panel_keyboard_main_menu=types.InlineKeyboardMarkup()
ap_btn_cp=types.InlineKeyboardButton("Make post", callback_data='create_post_admin')
ap_btn_dp=types.InlineKeyboardButton("Delete post", callback_data='delete_post_admin')
ap_btn_chp = types.InlineKeyboardButton("Change post", callback_data='change_post_admin')
ap_btn_mur = types.InlineKeyboardButton("Give a role to user", callback_data="make_user_role")
ap_btn_drfu = types.InlineKeyboardButton("Delete user role", callback_data="delete_user_role")
admin_panel_keyboard_main_menu.row(ap_btn_mur)
admin_panel_keyboard_main_menu.row(ap_btn_drfu)
admin_panel_keyboard_main_menu.row(ap_btn_chp)
admin_panel_keyboard_main_menu.row(ap_btn_cp, ap_btn_dp)