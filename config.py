import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
admin_id = os.getenv("ADMIN_ID")
admins = admin_id.split(',')
host = os.getenv("PGHOST")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")