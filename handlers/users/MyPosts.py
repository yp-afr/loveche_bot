from asyncio import sleep

from aiogram import types

from data import names
from handlers.users.misc import del_post, change_post_cb
from loader import dp
from utils.dp_api.database import database


@dp.message_handler(text_contains=names.button_myposts_text)
async def my_posts(message: types.Message):
    rows = await database.load_personal_posts()
    if rows:
        for row in rows:
            markup = types.InlineKeyboardMarkup(inline_keyboard=[
                [types.InlineKeyboardButton(text="Изменить", callback_data=change_post_cb.new(item_id=int(row['id']))),
                 types.InlineKeyboardButton(text="Удалить", callback_data=del_post.new(item_id=int(row['id'])))]
            ])
            text = "<b>" + row['type'] + "</b> -- " + row['category'] + "\n\n" + row['caption']
            if row['photo'] is None:
                await message.answer(text, reply_markup=markup)
            else:
                await message.answer_photo(photo=row['photo'], caption=text, reply_markup=markup)
            await sleep(0.3)
    else:
        await message.answer(names.zero_presonal_posts_message)
