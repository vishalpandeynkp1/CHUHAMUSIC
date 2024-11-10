#
# Copyright (C) 2024 by IamDvis@Github, < https://github.com/IamDvis >.
#
# This file is part of < https://github.com/IamDvis/DV-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/IamDvis/DV-MUSIC/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BANNED_USERS
from ERAVIBES import app
from ERAVIBES.core.call import ERA as ERA
from ERAVIBES.utils.database import is_music_playing, music_on
from ERAVIBES.utils.decorators import AdminRightsCheck


@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await ERA.resume_stream(chat_id)
    buttons_resume = [
        [
            InlineKeyboardButton(text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
        ],
    ]
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(buttons_resume),
    )


__MODULE__ = "Resume"
__HELP__ = """
**Resume**

This module allows administrators to resume playback of the currently paused track.

Commands:
- /resume: Resumes playback of the currently paused track for group.
- /cresume: Resumes playback of the currently paused track for channel.

Note:
- Only administrators can use these commands.
"""
