from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from data.config import admins
from keyboards.default import AdminMain
from loader import dp, bot
from utils.dp_api.database import database


@dp.message_handler(commands="menu", state='*', user_id=admins)
async def menu(message: types.Message, state: FSMContext):
    row = await database.get_admins()
    print(row)
    await state.reset_state()
    user_id = message.from_user.id
    chat_id = "@lovechernihiv"
    try:
        result = await bot.get_chat_member(chat_id, user_id)
        if result['status'] == 'left':
            await message.answer(names.unsubscribed_message, reply_markup=None)
        else:
            await message.answer(names.menu_text, reply_markup=AdminMain.markup)
    except Exception:
        pass
