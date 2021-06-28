import asyncio

from utils.dp_api.database import database


async def get_admins_list():
    admins = await database.get_admins()
    return admins


loop = asyncio.get_event_loop()
admins = loop.run_until_complete(get_admins_list())
