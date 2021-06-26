from aiogram import types

from handlers.users.misc import del_review
from loader import dp, bot
from utils.dp_api.database import database


@dp.callback_query_handler(del_review.filter())
async def delete_post(call: types.CallbackQuery, callback_data: dict):
    review_id = int(callback_data.get("review_id"))
    try:
        await database.del_review(review_id)
        chat_id = types.User.get_current().id
        msg_id = call.message.message_id
        await bot.delete_message(chat_id, msg_id)
    except Exception:
        await call.message.answer("Упс, что-то пошло не так!")
