from aiogram.utils import executor
from config.bot_config import dp
from handlers.admin_panel.create_post.create_post import *
from handlers.admin_panel.create_post.states_post.post_name import *
from handlers.admin_panel.create_post.states_post.post_disc import *
from handlers.admin_panel.create_post.states_post.post_tag import *
from handlers.admin_panel.create_post.states_post.post_link import *
from handlers.admin_panel.main_menu import *
from handlers.cm_panel.create_post.create_post import *
from handlers.cm_panel.create_post.states_post.post_name import *
from handlers.cm_panel.create_post.states_post.post_disc import *
from handlers.cm_panel.create_post.states_post.post_tag import *
from handlers.cm_panel.create_post.states_post.post_link import *
from handlers.cm_panel.main_menu import *
from handlers.start.start import *
from handlers.admin_panel.create_user_role.create_user_role import *
from handlers.admin_panel.create_user_role.admin.admin import *
from handlers.admin_panel.create_user_role.cm.cm import *
from handlers.admin_panel.delete_user_role.delete_user_role import *
from handlers.admin_panel.change_post.get_post import *
from handlers.admin_panel.change_post.states_change_post.post_disc import *
from handlers.admin_panel.change_post.states_change_post.post_id import *
from handlers.admin_panel.change_post.states_change_post.post_name import *
from handlers.admin_panel.change_post.states_change_post.post_tag import *
from handlers.admin_panel.change_post.states_change_post.post_link import *
from handlers.admin_panel.delete_post.delete_post import *
from handlers.admin_panel.delete_post.states_delete_post.post_id import *
from handlers.cm_panel.change_post.get_post import *
from handlers.cm_panel.change_post.states_change_post.post_disc import *
from handlers.cm_panel.change_post.states_change_post.post_id import *
from handlers.cm_panel.change_post.states_change_post.post_name import *
from handlers.cm_panel.change_post.states_change_post.post_tag import *
from handlers.cm_panel.change_post.states_change_post.post_link import *
from handlers.cm_panel.delete_post.delete_post import *
from handlers.cm_panel.delete_post.states_delete_post.post_id import *
from handlers.user_panel.create_user import *
from handlers.user_panel.view_posts import *
from handlers.user_panel.get_refferal_link import *
from handlers.user_panel.save_voice_message import *
from handlers.user_panel.back_to_main_menu_user import *
from handlers.user_panel.view_referrals import *
from handlers.admin_panel.get_referral_link import *
from handlers.admin_panel.view_referrals import *
from handlers.cm_panel.get_referral_link import *
from handlers.cm_panel.view_referrals import *
from handlers.payment.pay import *

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
