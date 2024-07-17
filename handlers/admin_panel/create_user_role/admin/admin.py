from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from bd_handlers.role.create_admin import create_admin
from bd_handlers.role.check_user_role import check_db_user_role

class FSM_create_user_role_admin(StatesGroup):
    user_id=State()
    user_name = State()

@dp.callback_query_handler(text="take_user_role_admin", state=None)
async def load_user_role_admin(callback_query: types.CallbackQuery):
    await FSM_create_user_role_admin.user_id.set()
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id, text=f"The role has been chosen\n\nEnter user ID of a person whom you want to make an admin")

@dp.message_handler(state=FSM_create_user_role_admin.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    
    try:
        float(message.text)
        test = await check_db_user_role(user_id=int(message.text))

        if test == 'admin':
            await state.finish()
            await bot.send_message(chat_id=message.from_user.id, text=f"\nError! User ID is already in use\n" f"\nThe user is an admin\n" f"\nTry again", reply_markup=admin_panel_keyboard_back_to_main_menu)
        elif test == 'cm':
            await state.finish()
            await bot.send_message(chat_id=message.from_user.id, text=f"\nError! User ID is already in use\n" f"\nThe user is a content manager\n" f"\nTry again", reply_markup=admin_panel_keyboard_back_to_main_menu)
    
        else:
            async with state.proxy() as data:
                data['user_id'] = message.text
                str_data = str(data['user_id'])
                int_data = int(str_data)
                
                if int_data < 0:
                    await state.finish()
                    await bot.send_message(chat_id=message.from_user.id, text=f"\nError! User ID cannot be a negative value\n"  f"\nTry again", reply_markup=admin_panel_keyboard_back_to_main_menu)
                else:
                    await FSM_create_user_role_admin.next()
                    await bot.send_message(chat_id=message.from_user.id, text=f"\nAdmin\n" f"User ID: {int_data}\n" f"\nEnter username: ")

    except ValueError:
        await state.finish()
        await bot.send_message(chat_id=message.from_user.id, text=f"\nError! User ID has to be a number\n" f"\nTry again", reply_markup=admin_panel_keyboard_back_to_main_menu)


@dp.message_handler(state=FSM_create_user_role_admin.user_name)
async def load_user_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        res = isinstance(message.text, str)
        if res:
            data['user_name'] = message.text
            int_data_user_id = int(data['user_id'])
            await state.finish()
            await create_admin(user_id=int_data_user_id, user_name=data['user_name'])
            await bot.send_message(chat_id=message.from_user.id, text=f"\nAdmin\n" f"User ID: {int_data_user_id}\n" f"Username: {data['user_name']}\n" f"Admin role created successfully", reply_markup=admin_panel_keyboard_back_to_main_menu)
        else:
            await state.finish()
            await bot.send_message(chat_id=message.from_user.id, text=f"\nError! Please enter a string\n" f"\nTry again", reply_markup=admin_panel_keyboard_back_to_main_menu)