from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from player.config import ASSISTANT_NAME as bn


@Client.on_callback_query(filters.regex("help"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{bn} to your group.
4.) turn on the voice chat first before start to stream video.
5.) type /stream (reply to video) to start video streaming.
6.) type /stop to end the video streaming.
7.) type /play<song name> to start audio play. 
8.) type /end to end audio play
9.) type /skip to skip audio play to next song. 
10.) type /pause to stop current audio play. 
11.) type /resume to start current audio play again. 

📝 **note: stream & stop command can only be executed by group admin only!**

⚡ __ᴘᴀʀᴛ ᴏꜰ `❛╚»🇹G⃠«╝🇳/🇽𝖣 ‌┈──̇─̇─̇─̇─••` ᴛᴇᴀᴍ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ʙᴀᴄᴋ", callback_data="cbstart")
      ]]
    ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"✨ **Hello there, I am a telegram video streaming bot.**\n\n💭 **I was created to stream videos in group video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ʜᴇʟᴘ", callback_data="help"), 
                          InlineKeyboardButton(
                             "👀 ᴄᴍᴅꜱ ʟɪꜱᴛ", callback_data="cblist")
                       ],[
                          InlineKeyboardButton(
                             "ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/TEAM-PATRICIA/PatriciaVideoPlayer")
                       ],[
                          InlineKeyboardButton(
                             "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/TGbotsXD"),
                          InlineKeyboardButton(
                             "🎑 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟꜱ", url="https://t.me/TGbotzXD")
                       ]]
                    ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **bot information !**

😇 __This bot was created to stream video in telegram group video chats using several methods from web Server.__

💡 __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots.__


__This bot licensed under GNU-GPL 3.0 License__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ʙᴀᴄᴋ", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )

@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""😏 ᴀʟʟ ᴄᴍᴅꜱ ʟɪꜱᴛ:

» /stream (reply to video or file) - to stream video or url of YouTube 
» /stop - end the video streaming
» /play (reply to audio file Or songname) - to stream audio play. 
» /pause - stop song play on current line
» /resume - start song play with current line
» /end stop music player
» /skip skip the current song to next selected
» /song (song name) - download song from YT
» /vsong (video name) - download video from YT
» /lyric (song name) - lyric scrapper

⚡ __ᴘᴀʀᴛ ᴏꜰ  ᴜᴘᴅᴀᴛᴇꜱ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ʙᴀᴄᴋ", callback_data="cbstart")
      ]]
    ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
