from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.AddAdmin import AddAdmin
from utils.dp_api.database import database


@dp.message_handler(state=AddAdmin.EnterID, text_contains="@")
async def add_admin(message: types.Message, state: FSMContext):
    try:
        await database.add_admin(message.text)
        await message.answer("Успешно!")
    except Exception:
        await message.answer("Что-то пошло не так, админ не был назначен")
    await state.reset_state()
