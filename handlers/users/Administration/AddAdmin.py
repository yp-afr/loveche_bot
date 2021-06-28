from aiogram import types

from loader import dp
from states.AddAdmin import AddAdmin


@dp.callback_query_handler(text_contains="set_admin")
async def set_admin(call: types.CallbackQuery):
    await call.message.answer("Введи id будущего админа, для того что бы узнать id необходимо отправить команду старт"
                              "боту @userinfobot")
    await AddAdmin.EnterID.set()
