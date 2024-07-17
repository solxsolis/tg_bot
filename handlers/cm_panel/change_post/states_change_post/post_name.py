from keyboards.cm_panel_keyboard_back_to_main_menu import cm_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.cm_panel.change_post.get_post import FSM_change_post_cm

@dp.message_handler(state=FSM_change_post_cm.post_name)
async def post_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_name'] = str(message.text)
        await FSM_change_post_cm.next()
        await bot.send_message(chat_id=message.from_user.id, text=f"Post ID: {data['key']}\n" f"Post name: {data['post_name']}\n" f"Enter new description: \n", reply_markup=cm_panel_keyboard_back_to_main_menu)
