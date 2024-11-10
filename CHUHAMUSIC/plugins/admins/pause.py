#
# Copyright (C) 2024 by vishalpandeynkp1@Github, < https://github.com/vishalpandeynkp1 >.
#
# This file is part of < https://github.com/vishalpandeynkp1/CHUHAMUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/vishalpandeynkp1//blob/master/LICENSE >
#
# All rights reserved.A
#

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BANNED_USERS
from  import app
from CHUHAMUSIC.core.call import CHUHA as CHUHA
from CHUHAMUSIC.utils.database import is_music_playing, music_off
from CHUHAMUSIC.utils.decorators import AdminRightsCheck


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await CHUHA.pause_stream(chat_id)

    buttons = [
        [
            InlineKeyboardButton(
                text="ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ʀᴇᴘʟᴀʏ", callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
    ]

    await message.reply_text(
        _["admin_2"].format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


__MODULE__ = "Pause"
__HELP__ = """
**Pause Music**

This module allows administrators to pause the music playback in the group.

Commands:
- /pause: Pause the music playback in groups.
- /cpause: Pause the music playback in channels.

Note:
- Only administrators can use these commands.
"""
