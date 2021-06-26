from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from loader import dp
from states.ChangeItem import ChangeItem
from utils.dp_api.database import database


@dp.message_handler(state=ChangeItem.ChangeCaption)
async def change_caption(message: types.Message, state: FSMContext):
    data = await state.get_data()
    item_id = data.get("item_id")
    msg: types.Message.message_id = data.get("msg")
    try:
        await database.change_item(message.text, item_id)
        await message.answer(names.successful_change_text)
        chat_id = types.User.get_current().id
        await message.edit_text(message.text)
    except Exception:
        pass
    await state.reset_state()
