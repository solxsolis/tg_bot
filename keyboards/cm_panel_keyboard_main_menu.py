from aiogram import types

cm_keyboard_main_menu = types.InlineKeyboardMarkup()

ap_btn_cp = types.InlineKeyboardButton('Make post', callback_data = 'create_post_cm')
ap_btn_dp = types.InlineKeyboardButton('Delete post', callback_data = 'delete_post_cm')
ap_btn_chp = types.InlineKeyboardButton('Change post', callback_data = 'change_post_cm')
ap_btn_rl = types.InlineKeyboardButton('Get referral link', callback_data='get_ref_link_cm')
ap_btn_vr = types.InlineKeyboardButton('View my refferals', callback_data='view_refs_cm')

cm_keyboard_main_menu.row(ap_btn_cp, ap_btn_dp)
cm_keyboard_main_menu.row(ap_btn_chp)
cm_keyboard_main_menu.row(ap_btn_rl, ap_btn_vr)