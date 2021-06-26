from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from keyboards.default import Main
from loader import dp, bot


@dp.message_handler(commands="menu", state='*')
async def menu(message: types.Message, state: FSMContext):
    await state.reset_state()
    user_id = message.from_user.id
    chat_id = "@lovechernihiv"
    try:
        result = await bot.get_chat_member(chat_id, user_id)
        if result['status'] == 'left':
            await message.answer(names.unsubscribed_message, reply_markup=None)
        else:
            await message.answer(names.menu_text, reply_markup=Main.markup)
    except Exception:
        pass
