from aiogram import types
from config.bot_config import dp, bot
from keyboards.user_panel_keyboard_back_to_main_menu import user_keyboard_back_to_main_menu
from bd_handlers.get_post.get_post import get_posts


@dp.callback_query_handler(text='view_posts')
async def user_panel_view_posts_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    rows = await get_posts()
    posts = []
    for x in rows:
        post = x
        post_id = x['key']
        post_name = x['post_name']
        post_disc = x['post_disc']
        post_link = x['post_link']
        post_tag = x['post_tag']
        post_string = f"<b>ID:</b>\n<i>{post_id}</i>\n"f"\n<b>Name:</b>\n<i>{post_name}</i>\n"f"\n<b>Description:</b>\n<i>{post_disc}</i>\n"f"\n<b>Link:</b>\n<i>{post_link}</i>\n"f"\n<b>Tag:</b>\n<i>#{post_tag}</i>\n"
        posts.append(post_string)
    num_posts = len(posts)
    if num_posts == 0:
        await bot.send_message(chat_id=callback_query.from_user.id, text=f'No posts\n')
    else:
        for post in posts:
            await bot.send_message(chat_id=callback_query.from_user.id, text=post, parse_mode = 'HTML', reply_markup=user_keyboard_back_to_main_menu)
