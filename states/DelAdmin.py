from aiogram.dispatcher.filters.state import StatesGroup, State


class DelAdmin(StatesGroup):
    EnterID = State()
