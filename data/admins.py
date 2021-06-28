from utils.dp_api.database import database

admins = await database.get_admins()
