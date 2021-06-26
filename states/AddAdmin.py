from aiogram.dispatcher.filters.state import StatesGroup, State


class AddAdmin(StatesGroup):
    EnterID = State()
