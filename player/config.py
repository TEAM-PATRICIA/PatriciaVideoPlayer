import os
from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
BOT_TOKEN = getenv("BOT_TOKEN", None)
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
SESSION_NAME = getenv("SESSION_NAME", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ?").split())
