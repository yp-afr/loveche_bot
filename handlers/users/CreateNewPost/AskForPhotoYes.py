from aiogram import types

from data import names
from loader import dp
from states.NewItem import NewItem


@dp.callback_query_handler(state=NewItem.AskForPhoto, text_contains="yes")
async def send_photo(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(names.send_photo_text)
    await NewItem.WithPhoto.set()
