from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.users.misc import change_post_cb
from loader import dp
from states.ChangeItem import ChangeItem


@dp.callback_query_handler(change_post_cb.filter())
async def change_post(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    item_id = int(callback_data.get("item_id"))
    await call.message.reply(f"Изменение текста поста № {item_id}\n\nВведите новый текст публикации:")
    await ChangeItem.ChangeCaption.set()
    msg_id = call.message.message_id
    await state.update_data(item_id=item_id, msg=msg_id)
