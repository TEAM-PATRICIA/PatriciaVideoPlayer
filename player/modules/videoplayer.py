import os
import re
import time
import ffmpeg
import asyncio
from os import path
from asyncio import sleep
from youtube_dl import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pytgcalls import GroupCallFactory
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from player.config import API_ID, API_HASH, SESSION_NAME, BOT_USERNAME
from player.helpers.decorators import authorized_users_only
from player.helpers.filters import command


STREAM = {8}
VIDEO_CALL = {}


ydl_opts = {
        "format": "best",
        "addmetadata": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "videoformat": "mp4",
        "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)

app = Client(SESSION_NAME, API_ID, API_HASH)
group_call_factory = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)


@Client.on_message(command(["stream", f"stream@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def vstream(client, m: Message):
    if 1 in STREAM:
        await m.reply_text("😕 **sorry, there's another video streaming right now**\n\n» **wait for it to finish then try again!**")
        return

    media = m.reply_to_message
    if not media and not ' ' in m.text:
        await m.reply("🔺 **please reply to a video or live stream url or youtube url to stream the video!**")

    elif ' ' in m.text:
        msg = await m.reply_text("🔄 **processing youtube url...**")
        text = m.text.split(' ', 1)
        url = text[1]
        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex,url)
        if match:
            await msg.edit("🔄 **starting youtube streaming...**")
            try:
                info = ydl.extract_info(url, False)
                ydl.download([url])
                ytvid = path.join("downloads", f"{info['id']}.{info['ext']}")
            except Exception as e:
                await msg.edit(f"❌ **youtube downloader error!** \n\n`{e}`")
                return
            await sleep(2)
            try:
                chat_id = m.chat.id
                group_call = group_call_factory.get_group_call()
                await group_call.join(chat_id)
                await group_call.start_video(ytvid)
                VIDEO_CALL[chat_id] = group_call
                await msg.edit(f"💡 **started [youtube streaming]({url}) !\n\n» join to video chat to watch the youtube stream.**")
                try:
                    STREAM.remove(0)
                except:
                    pass
                try:
                    STREAM.add(1)
                except:
                    pass
            except Exception as e:
                await msg.edit(f"❌ **something went wrong!** \n\nError: `{e}`")
        else:
            await msg.edit("🔄 **starting live streaming...**")
            live = url
            chat_id = m.chat.id
            await sleep(2)
            try:
                group_call = group_call_factory.get_group_call()
                await group_call.join(chat_id)
                await group_call.start_video(live)
                VIDEO_CALL[chat_id] = group_call
                await msg.edit(f"💡 **started [live streaming]({live}) !\n\n» join to video chat to watch the live stream.**")
                try:
                    STREAM.remove(0)
                except:
                    pass
                try:
                    STREAM.add(1)
                except:
                    pass
            except Exception as e:
                await msg.edit(f"❌ **something went wrong!** \n\nError: `{e}`")

    elif media.video or media.document:
        msg = await m.reply_text("📥 **downloading video...**\n\n💭 __this process will take quite a while depending on the size of the video.__")
        video = await client.download_media(media)
        chat_id = m.chat.id
        await sleep(2)
        try:
            group_call = group_call_factory.get_group_call()
            await group_call.join(chat_id)
            await group_call.start_video(video)
            VIDEO_CALL[chat_id] = group_call
            await msg.edit("💡 **video streaming started!**\n\n» **join to video chat to watch the video.**")
            try:
                STREAM.remove(0)
            except:
                pass
            try:
                STREAM.add(1)
            except:
                pass
        except Exception as e:
            await msg.edit(f"❌ **something went wrong!** \n\nError: `{e}`")
    else:
        await m.reply_text("🔺 **please reply to a video or live stream url or youtube url to stream the video!**")
        return


@Client.on_message(command(["stop", f"stop@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def vstop(client, m: Message):
    chat_id = m.chat.id
    if 0 in STREAM:
        await m.reply_text("😕 **no active streaming at this time**\n\n» start streaming by using /stream command (reply to video/yt url/live url)")
        return
    try:
        await VIDEO_CALL[chat_id].stop()
        await m.reply_text("🔴 **streaming has ended !**\n\n✅ __userbot has been disconnected from the video chat__")
        try:
            STREAM.remove(1)
        except:
            pass
        try:
            STREAM.add(0)
        except:
            pass
    except Exception as e:
        await m.reply_text(f"❌ **something went wrong!** \n\nError: `{e}`")
