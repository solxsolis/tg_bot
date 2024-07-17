from keyboards.cm_panel_keyboard_back_to_main_menu import cm_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.cm_panel.delete_post.delete_post import FSM_delete_post_cm
from bd_handlers.change_post.get_post_name import get_post_name
from bd_handlers.delete_post.delete_post import delete_post

@dp.message_handler(state=FSM_delete_post_cm.post_id)
async def post_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            row = await get_post_name(int(message.text))
            data['post_id'] = str(message.text)
            post_id = int(data['post_id'])
            await delete_post(post_id=post_id)
            await state.finish()
            await bot.send_message(chat_id=message.from_user.id, text=f"Post ID: {post_id}\nPost name: {row['post_name']}\nDeleted successfully", reply_markup=cm_panel_keyboard_back_to_main_menu)
        except TypeError:
            await state.finish()
            await bot.send_message(chat_id=message.from_user.id, text=f"Post ID: {message.text}\nError! This ID does not exist\nTry again", reply_markup=cm_panel_keyboard_back_to_main_menu)
        except ValueError:
            await state.finish()
            await bot.send_message(chat_id=message.from_user.id, text=f"Post ID: {message.text}\nError! Post ID has to be a number\nTry again", reply_markup=cm_panel_keyboard_back_to_main_menu)
