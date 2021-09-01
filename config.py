import os
from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
SESSION_NAME = getenv("SESSION_NAME", "session")
AUDIO_THUMBNAIL = getenv("AUDIO_THUMBNAIL", "")
VIDEO_THUMBNAIL = getenv("VIDEO_THUMBNAIL", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TGbotsXD")
