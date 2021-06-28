from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.exceptions import BadRequest

from keyboards.default import AdminMain
from data import names
from data.admins import admins
from loader import dp, bot


@dp.message_handler(CommandStart(), state='*', user_id=admins)
async def start(message: types.Message, state: FSMContext):
    await state.reset_state()
    user_id = message.from_user.id
    chat_id = "@lovechernihiv"
    try:
        result = await bot.get_chat_member(chat_id, user_id)
        if result['status'] == 'left':
            await message.answer(names.unsubscribed_message, reply_markup=None)
        else:
            await message.answer(names.subscribed_message, reply_markup=AdminMain.markup)
    except BadRequest:
        await message.answer(names.unsubscribed_message, reply_markup=None)
