from pyrogram import Client, idle
from player.config import API_ID, API_HASH, BOT_TOKEN
from player.modules.videoplayer import app


player = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="modules"),
)

player.start()
print("[INFO]: STARTING BOT CLIENT JOIN @TGBOTSXD || @TGBOTZXD")
app.start()
print("[INFO]: STARTING USERBOT CLIENT JOIN @TGBOTSXD || @TGBOTZXD")
idle()
