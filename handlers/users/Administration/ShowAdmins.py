from aiogram import types

from loader import dp
from utils.dp_api.database import database


@dp.callback_query_handler(text_contains="show_admins")
async def show_admins(call: types.CallbackQuery):
    # try:
    rows = await database.show_admins()
    print(rows)
    text = "<b>Список админов: \n</b>"
    if rows:
        for row in rows:
            text += f"{row['admin_id']}\n"
        await call.message.answer(text)
    else:
        await call.message.answer("Список назначенных админов пуст!")
