from aiogram import types

from data import names
from keyboards.inline import ShowAllPostsTypes
from loader import dp
from states.ShowItem import ShowItem


@dp.message_handler(text_contains=names.button_allposts_text)
async def show_items(message: types.Message):
    await message.answer(names.choose_type_text_all, reply_markup=ShowAllPostsTypes.markup)
    await ShowItem.ChooseType.set()
