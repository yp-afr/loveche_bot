from aiogram import types

from loader import dp
from states.DelAdmin import DelAdmin


@dp.callback_query_handler(text_contains="del_admin")
async def del_admin(call: types.CallbackQuery):
    await call.message.answer("Введи id")
    await DelAdmin.EnterID.set()
