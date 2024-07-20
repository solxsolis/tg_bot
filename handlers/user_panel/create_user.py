from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bd_handlers.role.create_user import create_user


class FSM_create_user(StatesGroup):
    user_name = State()

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'create_user')
async def admin_panel_delete_user_role(callback_query: types.CallbackQuery):
    await FSM_create_user.user_name.set()
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id, text=f"\nEnter a username: ")

@dp.message_handler(state=FSM_create_user.user_name)
async def load_user_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_name'] = message.text
        user_id = message.from_user.id
        await create_user(user_id=user_id, user_name=data['user_name'])
        await state.finish()
        await bot.send_message(chat_id=message.from_user.id, text=f"\Account created successfully")
     