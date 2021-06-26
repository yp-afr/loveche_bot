from aiogram import types

from data import names
from loader import dp
from states.NewReview import NewReview


@dp.callback_query_handler(state=NewReview.AskQuestion, text_contains="no_review")
async def choose_category(call: types.CallbackQuery):
    await call.message.answer(names.negative_review_text)
    await call.message.delete()
    await NewReview.EnterCaption.set()