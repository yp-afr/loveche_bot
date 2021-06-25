from aiogram.dispatcher.filters.state import StatesGroup, State

class NewItem(StatesGroup):
    CreateNew = State()
    ChooseType = State()
    ChooseCategory = State()
    EnterCaption = State()
    SetContact = State()
    SendPhoto = State()
    WithPhoto = State()
    WithOutPhoto = State()



class ChangeItem(StatesGroup):
    ChangeCaption = State()
    ChangePhoto = State()

class ShowItem(StatesGroup):
    ChooseType = State()
    ChooseCategory = State()

class AddAdmin(StatesGroup):
    EnterID = State()

class DelAdmin(StatesGroup):
    EnterID = State()
