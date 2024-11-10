#
# Copyright (C) 2024 by vishalpandeynkp1@Github, < https://github.com/vishalpandeynkp1 >.
#
# This file is part of < https://github.com/vishalpandeynkp1/CHUHAMUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/vishalpandeynkp1/CHUHAMUSIC/blob/master/LICENSE >
#
# All rights reserved.


from pyrogram import filters

import config
from strings import get_command
from CHUHAMUSIC import app
from CHUHAMUSIC.misc import SUDOERS
from CHUHAMUSIC.utils.database import add_off, add_on
from CHUHAMUSIC.utils.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@app.on_message(filters.command(LOGGER_COMMAND) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await add_on(config.LOG)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(config.LOG)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
