from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from handlers.users.misc import Item
from keyboards.inline import AskForPhotoCreatingPost
from loader import dp
from states.NewItem import NewItem


@dp.message_handler(state=NewItem.EnterCaption, content_types=types.ContentType.TEXT)
async def enter_caption(message: types.Message, state: FSMContext):
    caption = message.text
    data = await state.get_data()
    item: Item = data.get("item")
    item.caption = caption
    await message.answer(names.ask_photo_text, reply_markup=AskForPhotoCreatingPost.markup)
    await NewItem.AskForPhoto.set()
    await state.update_data(item=item)
