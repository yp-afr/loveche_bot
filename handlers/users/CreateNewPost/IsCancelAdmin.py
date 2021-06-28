from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from data.admins import admins
from keyboards.default import AdminMain
from loader import dp
from states.NewItem import NewItem


@dp.message_handler(state=NewItem, text_contains=names.button_cancel_text, user_id=admins)
async def check(message: types.Message, state: FSMContext):
    await message.answer(names.creating_post_canceled_text, reply_markup=AdminMain.markup)
    await state.reset_state()