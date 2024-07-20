from aiogram import types
from config.bot_config import dp, bot
from keyboards.user_panel_keyboard_back_to_main_menu import user_keyboard_back_to_main_menu
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import os


class FSM_save_voice(StatesGroup):
    waiting_for_voice = State()

@dp.callback_query_handler(text='send_voice')
async def user_panel_send_voice_callback(callback_query: types.CallbackQuery):
    await FSM_save_voice.waiting_for_voice.set()
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id, text=f'you can now send your voice message', reply_markup=user_keyboard_back_to_main_menu)

@dp.message_handler(content_types=types.ContentType.VOICE, state=FSM_save_voice.waiting_for_voice)
async def load_voice_message(message: types.Message, state: FSMContext):
    voice = message.voice
    file_info = await bot.get_file(voice.file_id)
    file_path = file_info.file_path

    save_directory = 'voice_messages'
    os.makedirs(save_directory, exist_ok=True)
    save_path = os.path.join(save_directory, f"{voice.file_id}.ogg")

    await bot.download_file(file_path, save_path)
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text="Your voice message has been saved", reply_markup=user_keyboard_back_to_main_menu)
