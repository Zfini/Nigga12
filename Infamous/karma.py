# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/8635b3e3d2950eb772ff3.jpg"
]

HEY_IMG = "https://telegra.ph/file/8635b3e3d2950eb772ff3.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/5378914b75358f5f4e234.mp4"
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ * ɪ ᴀᴍ ᴢᴇɴɪᴛsᴜ, ᴀ ᴅᴇᴍᴏɴ sʟᴀʏᴇʀ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="✙𝘼𝘿𝘿 𝙈𝙀✙",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 🌝", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="𝘿𝙀𝙏𝘼𝙄𝙇𝙎 ⚡", callback_data="Miko_"),
        InlineKeyboardButton(text="𝘼𝙄", callback_data="ai_handler"),
        
    ],
    [
        InlineKeyboardButton(text="𝘾𝙍𝙀𝘼𝙏𝙊𝙍 🥵", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="✙𝘼𝘿𝘿 𝙈𝙀✙",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝙎𝙐𝙋𝙋𝙊𝙍𝙏 👀", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="𝘾𝙍𝙀𝘼𝙏𝙊𝙍 🥵", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="𝙐𝙋𝘿𝘼𝙏𝙀𝙎", url="https://t.me/Hydra_Updates"),
        ib(text="𝙎𝙐𝙋𝙋𝙊𝙍𝙏", url="https://t.me/hydraXsupport"),
    ],
    [
        ib(
            text="✙𝘼𝘿𝘿 𝙈𝙀✙",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
⚡ *乙ᴇɴɪᴛsᴜ Ꭺɢᴀᴛsᴜᴍᴀ* ⚡

⏣ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
