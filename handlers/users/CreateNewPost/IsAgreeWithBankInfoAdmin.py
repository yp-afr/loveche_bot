from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import admins
from keyboards.default import AdminMain
from loader import dp
from states.NewItem import NewItem


@dp.callback_query_handler(state=NewItem.ChooseCategory, text_contains="agree", user_id=admins)
async def bank_agree(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Меню: ", reply_markup=AdminMain.markup)
    await state.reset_state()
