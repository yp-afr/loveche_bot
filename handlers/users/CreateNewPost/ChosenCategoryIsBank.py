from aiogram import types

from data import names
from keyboards.inline import BankInfoAgree
from loader import dp
from states.NewItem import NewItem


@dp.callback_query_handler(state=NewItem.ChooseCategory, text_contains="Bank")
async def bank_check(call: types.CallbackQuery):
    await call.message.edit_text(names.cat_bank_text, reply_markup=BankInfoAgree.markup)
