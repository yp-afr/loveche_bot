from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from data.config import admins
from handlers.users.misc import Item
from keyboards.default import AdminMain, Main
from loader import dp
from states.NewItem import NewItem
from utils.dp_api.database import database
from utils.misc.mailing import mailing


@dp.callback_query_handler(state=NewItem.AskForPhoto, text_contains="no")
async def without_photo(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    item: Item = data.get("item")
    record_id = await database.add_new_item(None, item.caption, item.type_finds, item.category, item.username)
    if record_id:
        if str(types.User.get_current().id) in admins:
            await call.message.answer(names.post_success_text, reply_markup=AdminMain.markup)
        else:
            await call.message.answer(names.post_success_text, reply_markup=Main.markup)
        await mailing(item.caption, item.type_finds, item.category, None, item.username)
    await state.reset_state()
