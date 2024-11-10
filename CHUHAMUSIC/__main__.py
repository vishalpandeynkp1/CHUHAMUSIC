#
# Copyright (C) 2024 by vishalpandeynkp1@Github, < https://github.com/vishalpandeynkp1 >.
#
# This file is part of < https://github.com/vishalpandeynkp1/CHUHAMUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/vishalpandeynkp1/CHUHAMUSIC/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib

from pyrogram import idle

import config
from config import BANNED_USERS
from CHUHAMUSIC import HELPABLE, LOGGER, app, userbot
from CHUHAMUSIC.core.call import CHUHA
from CHUHAMUSIC.plugins import ALL_MODULES
from CHUHAMUSIC.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("CHUHAMUSIC").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("CHUHAMUSIC").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("CHUHAMUSIC.plugins").info("Successfully Imported All Modules ")

    await userbot.start()
    await CHAHU.start()
    await CHAHU.decorators()
    LOGGER("CHUHAMUSIC").info("🎉 𝗖𝗛𝗨𝗛𝗔𝗠𝗨𝗦𝗜𝗖🥳𝗦𝗧𝗔𝗥𝗧𝗘𝗗🥳𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 🎊")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("CHUHAMUSIC").info("𝗦𝘁𝗼𝗽𝗽𝗶𝗻𝗴 𝗖𝗛𝗨𝗛𝗔𝗠𝗨𝗦𝗜𝗖! 𝗚𝗼𝗼𝗱𝗕𝘆𝗲 🥹")
