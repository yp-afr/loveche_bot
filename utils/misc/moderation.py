from asyncio import sleep

from data.admins import admins
from loader import bot
from utils.dp_api.database import database


async def moderation(caption, item_type, item_category, photo, author_):
    text = f"<b>Новый пост от пользователя!</b>\n\nВ разделе {item_type} -- {item_category}\n\n"
    text += caption
    text += f"\n\nКонтакты: {author_}"
    for admin in admins:
        if photo:
            await bot.send_photo(photo=photo, chat_id=admin, caption=text)
            await sleep(0.3)
        else:
            await bot.send_message(chat_id=admin, text=text)
            await sleep(0.3)
