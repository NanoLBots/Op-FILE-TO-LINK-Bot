#WOODcraft goel
from WOODcraft.bot import AngelBot
from WOODcraft.vars import Var
import logging
logger = logging.getLogger(__name__)
from WOODcraft.bot.plugins.stream import MY_PASS
from WOODcraft.utils.human_readable import humanbytes
from WOODcraft.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from WOODcraft.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                      
@AngelBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        await m.reply_photo(
            photo="https://graph.org/file/7200eb5f596ae3b17cfba.jpg",
            caption="**Hello⭐\n\nI will generate permanent download / stream links on your media**\n\n**Send /help for more details\n\nSend Me your media(Files/images/Videos) to start processing**",
            reply_markup=InlineKeyboardMarkup(
                [
                   [InlineKeyboardButton("Owner", url="https://t.me/botsnano"), InlineKeyboardButton("Leech Group", url="https://t.me/nano_leech")], 
                ]
            ),
            
        )
    else:

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**ᴛᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡\n\n📧 ғɪʟᴇ ɴᴀᴍᴇ :-\n{}\n {}\n\n💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- {}\n\n♻️ ᴛʜɪs ʟɪɴᴋ ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ɢᴇᴛ ᴇxᴘɪʀᴇᴅ ♻️\n\n<b>❖ YouTube.com/@Woodcraft5</b>**"
        await m.reply_text(            
            text=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ⚡", url=stream_link)]])
        )


@AngelBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
              
    await message.reply_photo(
            photo="https://graph.org/file/7200eb5f596ae3b17cfba.jpg",
            caption="**Send Me a Media and I will generate the download/streaming link for it**", 
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Owner", url="https://t.me/botsnano"), InlineKeyboardButton("Leech Group", url="https://t.me/nano_leech")],
                ]
            ),
            
        )

@AngelBot.on_message(filters.command('about') & filters.private)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    await message.reply_photo(
            photo="https://graph.org/file/7200eb5f596ae3b17cfba.jpg",
            caption="""<b>My Details</b>

<b>━━━━━━━File to link Bot</b>
<b>━━━━━━━a NANO BOT</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Owner", url="https://t.me/botsnano"), InlineKeyboardButton("Leech Group", url="https://t.me/nano_leech")],
                ]
            ),
            
        )
