from datetime import datetime
from asyncio import sleep

import aiogram.dispatcher.filters
from config import admins
import names
from names import *
from aiogram import types
from aiogram.utils.callback_data import CallbackData
from asyncpg import Connection, Record

import states
from load_all import bot, dp, db
from states import NewItem, ShowItem, AddAdmin, DelAdmin
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BadRequest
import markups

class Item:
    type_finds = ""
    category = ""
    photo = ""
    caption = ""
    username = ""


class DBCommands:
    pool: Connection = db
    ADD_NEW_ITEM = "INSERT INTO items(author_id,author_username, photo, caption, type, category, posted)" \
                   "VALUES($1,$2,$3,$4,$5,$6,$7) RETURNING id"
    LOAD_PERSONAL_POSTS = "SELECT * FROM items WHERE author_id=$1"
    DELETE_ITEM = "DELETE FROM items WHERE id=$1"
    CHANGE_ITEM = "UPDATE items SET caption=$1 WHERE id=$2"
    SHOW_ITEMS = "SELECT * FROM items WHERE type=$1 and category=$2"
    ADD_ADMIN = "INSERT INTO admins(admin_id) VALUES($1)"
    DEL_ADMIN = "DELETE FROM admins WHERE admin_id=$1"
    SHOW_ADMINS = "SELECT admin_id FROM admins"
    GET_ADMIN = "SELECT admin_id FROM admins WHERE admin_id=$1"
    GET_USERS = "SELECT * FROM items WHERE type=$1 and category=$2"
    GET_RECORD = "SELECT * FROM items WHERE id=$1"

    async def add_new_item(self, photo, caption, type_finds, category, author_username):
        author = types.User.get_current()
        author_id = author.id
        posted = datetime.now()
        args = author_id, author_username, photo, caption, type_finds, category, posted
        command = self.ADD_NEW_ITEM
        # try:
        record_id = await  self.pool.fetchval(command, *args)
        return record_id
    async def load_personal_posts(self):
        author_id = types.User.get_current().id
        command = self.LOAD_PERSONAL_POSTS
        rows = await self.pool.fetch(command, author_id)
        return rows
    async def delete_item(self, item_id):
        command = self.DELETE_ITEM
        await self.pool.execute(command, item_id)
    async def change_item(self,caption,item_id):
        command = self.CHANGE_ITEM
        args = caption, item_id
        await self.pool.execute(command, *args)
    async def show_items(self, type_finds, category):
        command = self.SHOW_ITEMS
        args = type_finds, category
        rows = await self.pool.fetch(command, *args)
        return rows
    async def add_admin(self, admin_id):
        command = self.ADD_ADMIN
        await self.pool.execute(command, admin_id)
    async def del_admin(self,admin_id):
        command = self.DEL_ADMIN
        await self.pool.execute(command,admin_id)
    async def show_admins(self):
        command = self.SHOW_ADMINS
        rows = await self.pool.fetch(command)
        return rows
    async def get_admin(self, admin_id):
        command = self.GET_ADMIN
        result = await database.pool.fetchval(command, admin_id)
        return result
    async def get_users(self, type_, category_):
        command = self.GET_USERS
        args = type_, category_
        result = await database.pool.fetch(command, *args)
        return result
    async def get_record(self, record_id):
        command = self.GET_RECORD
        result = await database.pool.fetch(command, record_id)
        return result

database = DBCommands()


@dp.message_handler(commands="start", state='*')
async def start(message: types.Message, state: FSMContext):
    await state.reset_state()
    user_id = message.from_user.id
    chat_id = "@lovechernihiv"
    try:
        result = await bot.get_chat_member(chat_id, user_id)
        if(result['status'] == 'left'):
            await message.answer(names.unsubscribed_message, reply_markup=None)
        else:
            if str(types.User.get_current().id) in admins:
                await message.answer(names.subscribed_message, reply_markup=markups.rplmarkup_admin)
            else:
                await message.answer(names.subscribed_message, reply_markup=markups.markup_main)
    except BadRequest:
        await message.answer(names.unsubscribed_message,reply_markup=None)

@dp.message_handler(commands="menu", state='*')
async def menu(message: types.Message, state: FSMContext):
    await state.reset_state()
    user_id = message.from_user.id
    chat_id = "@lovechernihiv"
    try:
        result = await bot.get_chat_member(chat_id, user_id)
        if (result['status'] == 'left'):
            await message.answer(names.unsubscribed_message, reply_markup=None)
        else:
            if str(types.User.get_current().id) in admins:
                await message.answer(names.menu_text, reply_markup=markups.rplmarkup_admin)
            else:
                await message.answer(names.menu_text, reply_markup=markups.markup_main)
    except Exception:
        pass


# Обработка кнопки создания поста

@dp.message_handler(text_contains=button_create_text)
async def create_new(message: types.Message):
    await message.answer(names.create_post_help_text,reply_markup=markups.markup_cancel)
    await message.answer(names.choose_type_text, reply_markup=markups.markup_types)
    await NewItem.ChooseType.set()

del_post = CallbackData("delete", "item_id")
change_post_cb = CallbackData("change", "item_id")

@dp.callback_query_handler(state=NewItem.ChooseType)
async def choose_type(call: types.CallbackQuery, state: FSMContext):
    type_finds = call.data[5:]
    item = Item()
    item.type_finds = type_finds
    if type_finds == "Найдено":
        await call.message.edit_text(choose_categorie_text, reply_markup=markups.markup_categories_found)
    elif type_finds == "Потеряно":
        await call.message.edit_text(choose_categorie_text, reply_markup=markups.markup_categories_lost)
    await NewItem.ChooseCategory.set()
    await state.update_data(item=item)

@dp.callback_query_handler(state=NewItem.ChooseCategory, text_contains="Bank")
async def bank_check(call: types.CallbackQuery, state: FSMContext):
    markup = types.InlineKeyboardMarkup(inline_keyboard=[[
        types.InlineKeyboardButton(text="Понятно", callback_data="agree")]])
    await call.message.edit_text(names.cat_bank_text,reply_markup=markup)

@dp.callback_query_handler(state=NewItem.ChooseCategory, text_contains="agree")
async def back_agree(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Меню: ", reply_markup=markups.markup_main)
    await state.reset_state()


@dp.callback_query_handler(state=NewItem.ChooseCategory)
async def choose_category(call: types.CallbackQuery, state: FSMContext):
    category = call.data[4:]
    data = await state.get_data()
    item: Item = data.get("item")
    item.category = category
    username = types.User.get_current().username
    if username:
        item.username = "@" + username
        await call.message.edit_reply_markup()
        await call.message.edit_text(names.enter_captiob_text)
        await NewItem.EnterCaption.set()
    else:
        await call.message.edit_reply_markup()
        await call.message.edit_text("Имя пользователя не было обнаружено, укажи пожалуйста свои контакты: ")
        await NewItem.SetContact.set()
    await state.update_data(item=item)

@dp.message_handler(state=NewItem,text_contains=button_cancel_text)
async def check(message: types.Message, state:FSMContext):
    if str(types.User.get_current().id) in admins:
        await message.answer(names.creating_post_canceled_text, reply_markup=markups.rplmarkup_admin)
    else:
        await message.answer(names.creating_post_canceled_text, reply_markup=markups.markup_main)
    await state.reset_state()

@dp.message_handler(state=NewItem.SetContact)
async def get_contact(message: types.Message, state: FSMContext):
    data = await state.get_data()
    item: Item = data.get("item")
    item.username = message.text
    await message.answer(names.enter_captiob_text)
    await NewItem.EnterCaption.set()
    await state.update_data(item=item)

@dp.message_handler(state=NewItem,text_contains=button_cancel_text)
async def check(message: types.Message, state:FSMContext):
    if str(types.User.get_current().id) in admins:
        await message.answer(names.creating_post_canceled_text, reply_markup=markups.rplmarkup_admin)
    else:
        await message.answer(names.creating_post_canceled_text, reply_markup=markups.markup_main)
    await state.reset_state()


@dp.message_handler(state=NewItem.EnterCaption, content_types=types.ContentType.TEXT)
async def enter_caption(message: types.Message, state: FSMContext):
    caption = message.text
    data = await state.get_data()
    item: Item = data.get("item")
    item.caption = caption

    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Да", callback_data="yes"),
         types.InlineKeyboardButton(text="Нет", callback_data="no")]
    ])
    await message.answer(names.ask_photo_text, reply_markup=markup)
    await NewItem.SendPhoto.set()
    await state.update_data(item=item)


async def mailing(caption, item_type, item_category, photo, author_):
    type_ = item_type
    if type_ == "Найдено":
        type_ = "Потеряно"
    elif type_ == "Потеряно":
        type_ = "Найдено"
    results = await database.get_users(type_, item_category)
    for result in results:
        text = f"<b>Новый пост относящийся к твоей категории!\n\n" \
               f"</b><b>{item_type}</b> -- {item_category}\n\n"
        try:
            if photo:
                text += caption
                text += f"\n\nКонтакты: {author_}"
                await bot.send_photo(photo=photo, chat_id=result['author_id'], caption=text)
                await sleep(0.3)
            else:
                text += caption
                text += f"\n\nКонтакты: {author_}"
                await bot.send_message(chat_id=result['author_id'], text=text)
                await sleep(0.3)
        except Exception:
            pass



@dp.callback_query_handler(state=NewItem.SendPhoto)
async def send_photo(call: types.CallbackQuery, state: FSMContext):
    answer = call.data
    await call.message.delete()
    if(answer == "yes"):
        await call.message.answer(names.send_photo_text)
        await NewItem.WithPhoto.set()
    else:
        data = await state.get_data()
        item: Item = data.get("item")
        record_id = await database.add_new_item(None, item.caption, item.type_finds, item.category, item.username)
        if record_id:
            if str(types.User.get_current().id) in admins:
                await call.message.answer(names.post_success_text, reply_markup=markups.rplmarkup_admin)
            else:
                await call.message.answer(names.post_success_text, reply_markup=markups.markup_main)
            await mailing(item.caption, item.type_finds, item.category, None, item.username)
        await state.reset_state()

@dp.message_handler(state=NewItem.WithPhoto, content_types=types.ContentType.PHOTO)
async def with_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    data = await state.get_data()
    item: Item = data.get("item")
    record_id = await database.add_new_item(photo, item.caption, item.type_finds, item.category, item.username)
    if record_id:
        if str(types.User.get_current().id) in admins:
            await message.answer(names.post_success_text, reply_markup=markups.rplmarkup_admin)
        else:
            await message.answer(names.post_success_text, reply_markup=markups.markup_main)
        await mailing(item.caption, item.type_finds, item.category, photo, item.username)
    # await message.answer(f"Success adding id: {record_id}")
    await state.reset_state()



# Обработка кнопки Мои посты

@dp.message_handler(text_contains=button_myposts_text)
async def my_posts(message: types.Message):
    rows = await database.load_personal_posts()
    if rows:
        for row in rows:
            markup = types.InlineKeyboardMarkup(inline_keyboard=[
                [types.InlineKeyboardButton(text="Изменить", callback_data=change_post_cb.new(item_id=int(row['id']))),
                 types.InlineKeyboardButton(text="Удалить", callback_data=del_post.new(item_id=int(row['id'])))]
            ])
            text = "<b>" + row['type'] + "</b> -- " + row['category'] + "\n\n" + row['caption']
            if(row['photo'] == None):
                await message.answer(text, reply_markup=markup)
            else:
                await message.answer_photo(photo=row['photo'], caption=text, reply_markup=markup)
            await sleep(0.3)
    else:
        await message.answer(names.zero_presonal_posts_message)

# Обработка кнопки выгрузки всех постов

@dp.message_handler(text_contains=button_allposts_text)
async def show_items(message: types.Message, state: FSMContext):
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Найдено", callback_data="type_Найдено"),
             types.InlineKeyboardButton(text="Потеряно", callback_data="type_Потеряно")]
        ]
    )
    await message.answer(choose_type_text_all, reply_markup=markup)
    await ShowItem.ChooseType.set()

@dp.callback_query_handler(state=ShowItem.ChooseType)
async def shitm_choose_type(call: types.CallbackQuery, state:FSMContext):
    type_finds = call.data[5:]
    await call.message.edit_text(choose_categorie_text,reply_markup=markups.markup_categories_lost)
    await ShowItem.ChooseCategory.set()
    await state.update_data(item_type=type_finds)

@dp.callback_query_handler(state=ShowItem.ChooseCategory)
async def shitm_choose_category(call: types.CallbackQuery, state: FSMContext):
    category = call.data[4:]
    data = await state.get_data()
    item_type = data.get("item_type")
    await call.message.delete()
    rows = await database.show_items(type_finds=item_type, category=category)
    if rows:
        result = await database.get_admin(f"@{types.User.get_current().username}")
        print(result)
        for row in rows:
            if result:
                markup = types.InlineKeyboardMarkup(inline_keyboard=[
                    [types.InlineKeyboardButton(text="Изменить",
                                                callback_data=change_post_cb.new(item_id=int(row['id']))),
                     types.InlineKeyboardButton(text="Удалить", callback_data=del_post.new(item_id=int(row['id'])))]
                ])
            else:
                markup = None
            if (row['photo'] == None):
                await call.message.answer(f"<b>{row['type']}</b> -- {row['category']}\n\n{row['caption']}\n"
                                          f"\nКонтакты: {row['author_username']}", reply_markup=markup)
            else:
                await call.message.answer_photo(photo=row['photo'],
                                                caption=f"<b>{row['type']}</b> -- {row['category']}\n\n{row['caption']}"
                                                        f"\n\nКонтакты: {row['author_username']}", reply_markup=markup)
            await sleep(0.3)
    else:
        await call.message.answer(f"В категории <b>{item_type}->{category}</b> нет постов")
    await state.reset_state()

@dp.message_handler(text_contains=button_admin_text)
async def admin(message: types.Message):
    if str(types.User.get_current().id) in admins:
        await message.answer("Опции: ", reply_markup=markups.markup_admin)
    else:
        pass

@dp.callback_query_handler(text_contains="set_admin")
async def set_admin(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введи @юзернейм")
    await AddAdmin.EnterID.set()

@dp.message_handler(state=AddAdmin.EnterID, text_contains="@")
async def add_admin(message: types.Message, state: FSMContext):
    try:
        await database.add_admin(message.text)
        await message.answer("Успешно!")
    except Exception:
        await message.answer("Что-то пошло не так, админ не был назначен")
    await state.reset_state()

@dp.callback_query_handler(text_contains="del_admin")
async def del_admin(call: types.CallbackQuery):
    await call.message.answer("Введи @юзернейм")
    await DelAdmin.EnterID.set()

@dp.message_handler(state=DelAdmin.EnterID,  text_contains="@")
async def delete_admin(message: types.Message, state: FSMContext):
    try:
        await database.del_admin(message.text)
        await message.answer("Успешно!")
    except Exception:
        await message.answer("Что-то пошло не так, админ не был назначен!")
    await state.reset_state()

@dp.callback_query_handler(text_contains="show_admins")
async def show_admins(call: types.CallbackQuery, state: FSMContext):
    #try:
    rows = await database.show_admins()
    print(rows)
    text = "<b>Список админов: \n</b>"
    if rows:
        for row in rows:
            text += f"{row['admin_id']}\n"
        await call.message.answer(text)
    else:
        await call.message.answer("Список назначенных админов пуст!")
    #except Exception:
        #await call.message.answer("Что-то пошло не так!")


@dp.callback_query_handler(del_post.filter())
async def delete_post(call: types.CallbackQuery, callback_data: dict):
    item_id = int(callback_data.get("item_id"))
  #  message_id = int(callback_data.get("message_id"))
    await database.delete_item(item_id)
    chat_id = types.User.get_current().id
    msg_id = call.message.message_id
    await bot.delete_message(chat_id, msg_id)
@dp.callback_query_handler(change_post_cb.filter())
async def change_post(call: types.CallbackQuery, callback_data:dict, state: FSMContext):
    item_id = int(callback_data.get("item_id"))
    await call.message.answer(f"Изменение текста поста № {item_id}\n\nВведите новый текст публикации:")
    await states.ChangeItem.ChangeCaption.set()
    msg_id = call.message.message_id
    await state.update_data(item_id = item_id, msg=msg_id)

@dp.message_handler(state=states.ChangeItem.ChangeCaption)
async def change_caption(message: types.Message, state:FSMContext):
    data = await state.get_data()
    item_id = data.get("item_id")
    msg: types.Message.message_id = data.get("msg")
    try:
        await database.change_item(message.text, item_id)
        await message.answer(names.successful_change_text)
        chat_id = types.User.get_current().id
        await message.edit_text(message.text)
    except Exception:
        pass
    await state.reset_state()

