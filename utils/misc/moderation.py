from asyncio import sleep

from aiogram import types

from data.admins import admins
from handlers.users.misc import change_post_cb, del_post
from loader import bot
from utils.dp_api.database import database


async def moderation(caption, item_type, item_category, photo, author_, post_id):
    text = f"<b>Новый пост от пользователя!</b>\n\nВ разделе {item_type} -- {item_category}\n\n"
    text += caption
    text += f"\n\nКонтакты: {author_}"
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Изменить",
                                    callback_data=change_post_cb.new(item_id=int(post_id))),
         types.InlineKeyboardButton(text="Удалить", callback_data=del_post.new(item_id=int(post_id)))]
    ])
    for admin in admins:
        if photo:
            await bot.send_photo(photo=photo, chat_id=admin, caption=text, reply_markup=markup)
            await sleep(0.3)
        else:
            await bot.send_message(chat_id=admin, text=text, reply_markup=markup)
            await sleep(0.3)
