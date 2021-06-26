from aiogram import types

from handlers.users.misc import del_post
from loader import dp, bot
from utils.dp_api.database import database


@dp.callback_query_handler(del_post.filter())
async def delete_post(call: types.CallbackQuery, callback_data: dict):
    item_id = int(callback_data.get("item_id"))
    await database.delete_item(item_id)
    chat_id = types.User.get_current().id
    msg_id = call.message.message_id
    await bot.delete_message(chat_id, msg_id)
