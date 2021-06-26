from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from loader import dp
from states.NewReview import NewReview
from utils.dp_api.database import database


@dp.message_handler(state=NewReview.EnterCaption, content_types=types.ContentType.TEXT)
async def enter_caption_review(message: types.Message, state: FSMContext):
    caption = message.text
    await database.add_new_review(caption)
    await state.reset_state()