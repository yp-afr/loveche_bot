from aiogram import types

from data import names
from keyboards.inline import CreatingReview
from loader import dp
from states.NewReview import NewReview


@dp.message_handler(text_contains=names.button_create_review)
async def create_new_review(message: types.Message):
    await message.answer(names.choose_answer_review_text, reply_markup=CreatingReview.markup)
    await NewReview.AskQuestion.set()
