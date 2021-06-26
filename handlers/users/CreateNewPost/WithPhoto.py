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


@dp.message_handler(state=NewItem.WithPhoto, content_types=types.ContentType.PHOTO)
async def with_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    data = await state.get_data()
    item: Item = data.get("item")
    record_id = await database.add_new_item(photo, item.caption, item.type_finds, item.category, item.username)
    if record_id:
        if str(types.User.get_current().id) in admins:
            await message.answer(names.post_success_text, reply_markup=AdminMain.markup)
        else:
            await message.answer(names.post_success_text, reply_markup=Main.markup)
        await mailing(item.caption, item.type_finds, item.category, photo, item.username)
    await state.reset_state()
