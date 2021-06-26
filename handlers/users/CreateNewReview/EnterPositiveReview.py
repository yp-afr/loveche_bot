from aiogram import types

from data import names
from loader import dp
from states.NewReview import NewReview


@dp.callback_query_handler(state=NewReview.AskQuestion, text_contains="yes_review")
async def choose_category(call: types.CallbackQuery):
    await call.message.answer(names.positive_review_text)
    await NewReview.EnterCaption.set()
