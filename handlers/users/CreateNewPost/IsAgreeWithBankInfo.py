from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import Main
from loader import dp
from states.NewItem import NewItem


@dp.callback_query_handler(state=NewItem.ChooseCategory, text_contains="agree")
async def bank_agree(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Меню: ", reply_markup=Main.markup)
    await state.reset_state()
