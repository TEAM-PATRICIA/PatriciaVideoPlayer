import requests
from pyrogram import Client
from player.config import BOT_USERNAME
from player.helpers.filters import command

@Client.on_message(command(["asupan", f"asupan@{BOT_USERNAME}"]))
async def asupan(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("failed to get asupan from server...")


@Client.on_message(command(["wibu", f"wibu@{BOT_USERNAME}"]))
async def wibu(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("failed to get wibu from server...")


@Client.on_message(command(["chika", f"chika@{BOT_USERNAME}"]))
async def chika(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("failed to get chika from server...")


@Client.on_message(command(["truth", f"truth@{BOT_USERNAME}"]))
async def truth(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("something went wrong...")


@Client.on_message(command(["dare", f"dare@{BOT_USERNAME}"]))
async def dare(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("something went wrong...")


@Client.on_message(command(["lyric", f"lyric@{BOT_USERNAME}"]))
async def lirik(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**give a lyric name too !**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("🔎 **searching lyrics...**")
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("**Lyrics not found.** please give a valid song name !")
