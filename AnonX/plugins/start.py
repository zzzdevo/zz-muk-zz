import asyncio
from pyrogram.types import *
from pyrogram import filters, Client
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from pyrogram.enums import ChatType, ParseMode
import config
import redis
from pyrogram import *
from config import (OWNER_ID,
                    USER_OWNER,
                    MUSIC_BOT_NAME,
                    SUPPORT_CHANNEL,
                    BOT_TOKEN,
                    BANNED_USERS)
from strings import get_command, get_string
from AnonX import Telegram, YouTube, app
from AnonX.misc import SUDOERS, _boot_
from AnonX.plugins.playlist import del_plist_msg
from AnonX.plugins.sudoers import sudoers_list
from AnonX.utils.database import (add_served_chat,
                                  add_served_user,
                                  get_served_chats,
                                  get_served_users,
                                  blacklisted_chats,
                                  get_assistant, get_lang,
                                  get_userss, is_on_off,
                                  is_served_private_chat)
from AnonX.utils.decorators.language import LanguageStart
from AnonX.utils.inline import (help_pannel, private_panel,
                                start_pannel)

loop = asyncio.get_running_loop()
token = (BOT_TOKEN)
bot_id = app.bot_token.split(":")[0]
r = redis.from_url('redis://')
owner = (OWNER_ID)
dev_owner = int(6275847466)


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    global thumbnail, channel
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            dev = (OWNER_ID, 6275847466)

            keyboard = help_pannel(_)
            user = message.from_user.id
            if int(user) == dev_owner:
                await message.reply(
                    f"**𖢿 | : مرحبا حبيبي الوسكي مطور السورس{message.from_user.mention}\n𖢿 | : كل اقسام التحكم بالبوتات\n𖢿 | : تستطيع التحكم بكل البوتات عن طريق هذه الازرار**",
                    reply_markup=OwnerM)

            elif message.from_user.id in owner:

                await message.reply(
                    f"**𖢿 | : مرحبا عزيزي المطور الاساسي {message.from_user.mention}\n𖢿 | : اليك ازرار التحكم بالاقسام\n𖢿 | : تستطيع التحكم بجميع الاقسام فقط اضغط على القسم الذي تريده**",
                    reply_markup=main_dev_key)


            else:
                await message.reply_text(
                    f"**•⎆┊بەخێربێی ئەزیزم {message.from_user.mention}\n\n بۆ بۆتی گۆرانی {MUSIC_BOT_NAME} تایبەت بە @{USER_OWNER} \n\nپڕیەتی لە تایبەتمەندی و جوانکاری، زۆر خێرایە پشتگیری هەموو شوێنێك دەکات⚡️\n بۆت بکە ئەدمین و وە ڕۆڵی پێ بدە♥️**",
                    reply_markup=Owneruser)
                return await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["help_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
                )

        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])

        if name[0:3] == "sta":
            m = await message.reply_text(
                f"🥱 يتم جلب الاحصائيات الخاصه لـ {config.MUSIC_BOT_NAME} sᴇʀᴠᴇʀ."
	@@ -155,7 +157,8 @@ def get_stats():
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name == "verify":
            await message.reply_text(
                f"ʜᴇʏ {message.from_user.first_name},\nشكرا لوثوقك في انا  {config.MUSIC_BOT_NAME}, تم تخزين بياناتك اللازمه يمكنك التشغيل الان")
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
	@@ -188,7 +191,7 @@ def get_stats():
⏳ **ماوە : {duration} خولەك **
👀 **بینینەکان :** `{views}` **
🪐 **بڵاوکراوەتەوە لە : {published} **
🔗 **لینك : [لە یوتوب سەیری بکەن] **({link}) **
🎥 **که‌ناڵ :** [{channel}]({channellink})**
**🕷️ گەڕانی بەهێز لەلایەن {config.MUSIC_BOT_NAME} **"""
	@@ -199,7 +202,7 @@ def get_stats():
                            text="• ʏᴏᴜᴛᴜʙᴇ •", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="• sᴜᴩᴩᴏʀᴛ •", url="https://t.me/IQSUPP"
                        ),
                    ],
                ]
	@@ -228,22 +231,28 @@ def get_stats():
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                owner = (OWNER_ID)
                user = message.from_user.id
                if int(user) == dev_owner:
                    return await message.reply(
                        f"**𖢿 | : مرحبا حبيبي الوسكي مطور السورس{message.from_user.mention}\n𖢿 | : كل اقسام التحكم بالبوتات\n𖢿 | : تستطيع التحكم بكل البوتات عن طريق هذه الازرار**",
                        reply_markup=OwnerM)
                if message.from_user.id in owner:
                    return await message.reply_text(
                        f"**𖢿 | : مرحبا عزيزي المطور الاساسي {message.from_user.mention}\n𖢿 | : اليك ازرار التحكم بالاقسام\n𖢿 | : تستطيع التحكم بجميع الاقسام فقط اضغط على القسم الذي تريده**",
                        reply_markup=main_dev_key)
                else:
                    await message.reply_text(
                        f"**•⎆┊بەخێربێی ئەزیزم {message.from_user.mention}\n\n بۆ بۆتی گۆرانی {MUSIC_BOT_NAME} تایبەت بە @{USER_OWNER} \n\nپڕیەتی لە تایبەتمەندی و جوانکاری، زۆر خێرایە پشتگیری هەموو شوێنێك دەکات⚡️\n بۆت بکە ئەدمین و وە ڕۆڵی پێ بدە♥️**",
                        reply_markup=Owneruser)
                    return await message.reply_photo(
                        photo=config.START_IMG_URL,
                        caption=_["start_2"].format(
                            config.MUSIC_BOT_NAME
                        ),
                        reply_markup=InlineKeyboardMarkup(out),
                    )

            except:
                await message.reply_text(
                    _["start_2"].format(config.MUSIC_BOT_NAME),
	@@ -261,7 +270,7 @@ def get_stats():
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ضغط ستارت في البوت.\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
            )


@app.on_message(
    filters.command(get_command("START_COMMAND"))
	@@ -273,8 +282,8 @@ async def testbot(client, message: Message, _):
    OWNER = OWNER_ID[0]
    out = start_pannel(_, app.username, OWNER)
    return await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
	@@ -340,69 +349,9 @@ async def welcome(client, message: Message):
            return


Owneruser = ReplyKeyboardMarkup([
    [("فەرمان"), ("سەرچاوە")], [("سەرۆک"), ("گەشەپێدەر"), ("/help")],
    [("گۆرانی"), ("ڤیدیۆ"), ("وێنە")],
    [("زکر"), ("تایبەتمەندی"), ("زیرەکی دەستکرد")],
    [("یاری"), ("وێنەی کچان"), ("ق")]
], resize_keyboard=True)
