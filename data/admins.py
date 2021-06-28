from utils.dp_api.database import database


async def get_admins_list():
    list_admins = await database.get_admins()
    return list_admins

admins = get_admins_list()