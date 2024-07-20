from aiogram import types
from config.bot_config import dp, bot
from keyboards.user_panel_keyboard_back_to_main_menu import user_keyboard_back_to_main_menu
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
import uuid

config = dotenv_values(CONFIG_DIR / '.env')
payment_token = config['PAYMENT_TOKEN']

price = types.LabeledPrice(label='test payment', amount= 100 * 100)

def generate_start_parameter():
    return str(uuid.uuid4())

@dp.callback_query_handler(text='pay')
async def user_make_payment_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    start_parameter = generate_start_parameter()
    await bot.send_invoice(chat_id=callback_query.from_user.id,
                           title = 'Test payment',
                           description='This is a test payment, you will not be charged',
                           provider_token=payment_token,
                           currency='RUB',
                           prices=[price],
                           start_parameter=start_parameter,
                           payload = f"inv_{start_parameter}")
    
@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    successful_payment = message.successful_payment
    payload = successful_payment.invoice_payload
    await bot.send_message(chat_id=message.from_user.id, text="Payment successful", reply_markup=user_keyboard_back_to_main_menu)