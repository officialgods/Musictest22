from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ANNIEMUSIC import app
from config import BOT_USERNAME

start_txt = """**
ʀᴇᴘᴏ ᴄʜᴀɪʏᴇ ᴊᴀʟᴅɪ sᴇ ʟᴇʟᴏ ɴʜɪ ᴛᴏ ᴘsʏᴄʜᴏ ʜᴀᴛᴀᴅᴇɢᴀ
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙᴇs✪", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/OG_LORD_PSYCHO"),
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/XPROBOTS_SUPPORT"),
             ],
     
             [
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/RGB_FED_APPEAL"),          
             InlineKeyboardButton("︎ᴍᴜsɪᴄ", url=f"https://t.me/+iykYn9bXb0NkOGFl"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/r940l7.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
