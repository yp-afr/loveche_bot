from asyncio import sleep

from aiogram import types

from data import names
from data.config import admins
from loader import dp
from utils.dp_api.database import database


@dp.message_handler(text_contains=names.button_show_reviews, user_id=admins)
async def get_reviews(message: types.Message):
    rows = await database.get_reviews()
    if rows:
        for row in rows:
            text = str(row['caption']) + "\n\n"
            text += f"<a href='tg://user?id={row['author_id']}'>Автор отзыва</a>"
            await message.answer(text)
            await sleep(0.3)
    else:
        await message.answer("Пусто!")
