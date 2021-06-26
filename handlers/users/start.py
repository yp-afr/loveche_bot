from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.exceptions import BadRequest

from data import names
from keyboards.default import Main
from loader import bot, dp


@dp.message_handler(CommandStart(), state='*')
async def start(message: types.Message, state: FSMContext):
    await state.reset_state()
    user_id = message.from_user.id
    chat_id = "@lovechernihiv"
    try:
        result = await bot.get_chat_member(chat_id, user_id)
        if result['status'] == 'left':
            await message.answer(names.unsubscribed_message, reply_markup=None)
        else:
            await message.answer(names.subscribed_message, reply_markup=Main.markup)
    except BadRequest:
        await message.answer(names.unsubscribed_message, reply_markup=None)
