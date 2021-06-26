from aiogram import types

from data import names
from keyboards.default import Cancel
from keyboards.inline import CreatingPostTypes
from loader import dp
from states.NewItem import NewItem


@dp.message_handler(text_contains=names.button_create_text)
async def create_new(message: types.Message):
    await message.answer(names.create_post_help_text, reply_markup=Cancel.markup)
    await message.answer(names.choose_type_text, reply_markup=CreatingPostTypes.markup)
    await NewItem.ChooseType.set()
