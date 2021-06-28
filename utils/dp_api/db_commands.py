from datetime import datetime

from aiogram import types
from asyncpg import Connection

from loader import db


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
    ADD_NEW_REVIEW = "INSERT INTO reviews(author_id, caption, posted) VALUES($1,$2,$3)"
    GET_REVIEWS = "SELECT * FROM reviews"
    DEL_REVIEW = "DELETE FROM reviews WHERE id=$1"

    async def get_admins(self):
        command = self.SHOW_ADMINS
        row = self.pool.fetch(command)
        return row

    async def add_new_review(self, caption):
        author_id = types.User.get_current().id
        posted = datetime.now()
        args = author_id, caption, posted
        command = self.ADD_NEW_REVIEW
        await self.pool.execute(command, *args)

    async def del_review(self, review_id):
        command = self.DEL_REVIEW
        await self.pool.execute(command, review_id)

    async def get_reviews(self):
        command = self.GET_REVIEWS
        rows = await self.pool.fetch(command)
        return rows

    async def add_new_item(self, photo, caption, type_finds, category, author_username):
        author = types.User.get_current()
        author_id = author.id
        posted = datetime.now()
        args = author_id, author_username, photo, caption, type_finds, category, posted
        command = self.ADD_NEW_ITEM
        # try:
        record_id = await self.pool.fetchval(command, *args)
        return record_id

    async def load_personal_posts(self):
        author_id = types.User.get_current().id
        command = self.LOAD_PERSONAL_POSTS
        rows = await self.pool.fetch(command, author_id)
        return rows

    async def delete_item(self, item_id):
        command = self.DELETE_ITEM
        await self.pool.execute(command, item_id)

    async def change_item(self, caption, item_id):
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

    async def del_admin(self, admin_id):
        command = self.DEL_ADMIN
        await self.pool.execute(command, admin_id)

    async def show_admins(self):
        command = self.SHOW_ADMINS
        rows = await self.pool.fetch(command)
        return rows

    async def get_admin(self, admin_id):
        command = self.GET_ADMIN
        result = await self.pool.fetchval(command, admin_id)
        return result

    async def get_users(self, type_, category_):
        command = self.GET_USERS
        args = type_, category_
        result = await self.pool.fetch(command, *args)
        return result

    async def get_record(self, record_id):
        command = self.GET_RECORD
        result = await self.pool.fetch(command, record_id)
        return result
