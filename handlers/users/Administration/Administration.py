from aiogram import types

from data import names
from data.config import admins
from keyboards.inline import Administration
from loader import dp


@dp.message_handler(text_contains=names.button_admin_text, user_id=admins)
async def admin(message: types.Message):
    await message.answer("Опции: ", reply_markup=Administration.markup)
