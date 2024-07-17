from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from bd_handlers.role.delete_user_role import delete_user_role

class FSM_delete_role_from_user(StatesGroup):
    user_id = State()

@dp.callback_query_handler(text='delete_user_role')
async def admin_panel_delete_user_role(callback_query: types.CallbackQuery):
    await FSM_delete_role_from_user.user_id.set()
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id, text=f"\nEnter user ID of a person whose role you want to delete: ")

@dp.message_handler(state=FSM_delete_role_from_user.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.text
        str_data = str(data['user_id'])

        try:
            float(str_data)
            int_data = int(str_data)
            if int_data < 0:
                await state.finish()
                await bot.send_message(chat_id=message.from_user.id, text=f"\nError! User ID cannot be a negative value\n" f"\nTry again", reply_markup=admin_panel_keyboard_back_to_main_menu)
            else:
                await delete_user_role(user_id=int_data)
                await state.finish()
                await bot.send_message(chat_id=message.from_user.id, text=f"\nUser role deleted", reply_markup=admin_panel_keyboard_back_to_main_menu)
        except ValueError:
            await state.finish()
            await bot.send_message(chat_id=message.from_user.id, text=f"\nError! User ID has to be a number\n" f"\nTry again", reply_markup=admin_panel_keyboard_back_to_main_menu)
        except TypeError:
            await state.finish()
            await bot.send_message(chat_id=message.from_user.id, text=f"User ID: {message.text}\nError! This ID does not exist\nTry again", reply_markup=admin_panel_keyboard_back_to_main_menu)
        