from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""⎈¦ اهلا بـك عزيـزي المستخـدم

⎈¦ يمكنك استـخـراج التالـي

⎈¦ تيرمڪس تليثون للحسابات

⎈¦ تيرمـكـس تليثون للبوتـات

⎈¦ بايـروجـرام مـيوزك للحسابات

⎈¦ بايـروجـرام مـيوزك للبوتات

⎈¦ تم انشاء البوت بواسطة [𓌹 ↱ 𝘿ٓ𝙀ٓ𝙑ٰٰ 𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙 ↲ 𓌺](https://t.me/Mvhmed)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="إضغط لبدا استخراج الكود", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙", url="https://t.me/Mvhmed"),
                    InlineKeyboardButton("𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
