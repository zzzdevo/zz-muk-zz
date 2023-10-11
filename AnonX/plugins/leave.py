from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from AnonX import app
from AnonX.misc import SUDOERS
from strings.filters import command


@app.on_message(command(['leave', 'لێفتکە']) & SUDOERS)
async def leave_a_chat(client, message):
    if len(message.command) == 1: return await message.reply('**ئایدی گرووپم پێبدە**')
    chat = message.command[1]
    try: chat = int(chat)
    except: chat = chat
    try:
        buttons = [[InlineKeyboardButton('گرووپی بۆت', url=f'https://t.me/IQSUPP')]]
        await client.send_message(chat_id=chat, text='<b>ببورە بەڕیزم\nخاوەنەکەم پێی وتم کە دەربچم لەم گرووپە بۆ هەر کێشەیەك سەردانی گرووپی بۆت بکە</b>', reply_markup=InlineKeyboardMarkup(buttons))
        await client.leave_chat(chat)
    except Exception as e:
        await message.reply(f'**هەڵە: {e} **')
