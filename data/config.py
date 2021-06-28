import os

from dotenv import load_dotenv

from utils.dp_api.database import database

load_dotenv()

TOKEN = os.getenv("TOKEN")
admins = [
    database.get_admins()
]
print(admins)
host = os.getenv("PGHOST")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
