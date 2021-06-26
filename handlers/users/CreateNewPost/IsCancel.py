from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from keyboards.default import Main
from loader import dp
from states.NewItem import NewItem


@dp.message_handler(state=NewItem, text_contains=names.button_cancel_text)
async def check(message: types.Message, state: FSMContext):
    await message.answer(names.creating_post_canceled_text, reply_markup=Main.markup)
    await state.reset_state()
