from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from handlers.users.misc import Item
from loader import dp
from states.NewItem import NewItem


@dp.callback_query_handler(state=NewItem.AskForPhoto, text_contains="yes")
async def send_photo(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()
    item: Item = data.get("item")
    if item.category == 'Документы':
        await call.message.answer(names.send_photo_document_text)
    else:
        await call.message.answer(names.send_photo_text)
    await NewItem.WithPhoto.set()
