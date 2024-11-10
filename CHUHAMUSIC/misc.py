#
# Copyright (C) 2024 by vishalpandeynkp1@Github, < https://github.com/vishalpandeynkp1 >.
#
# This file is part of < https://github.com/vishalpandeynkp1/CHUHAMUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/vishalpandeynkp1/CHUHAMUSIC/blob/master/LICENSE >
#
# All rights reserved.

import socket
import time

import heroku3
from pyrogram import filters

import config
from CHUHAMUSIC.core.mongo import pymongodb

from .logging import LOGGER

SUDOERS = filters.user()


HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def dbb():
    global db
    global clonedb
    db = {}
    clonedb = {}
    LOGGER(__name__).info(f"𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗜𝗻𝗶𝘁𝗶𝗮𝗹𝗶𝘇𝗲𝗱...")


def sudo():
    global SUDOERS
    OWNER = config.OWNER_ID
    if config.MONGO_DB_URI is None:
        for user_id in OWNER:
            SUDOERS.add(user_id)
    else:
        sudoersdb = pymongodb.sudoers
        sudoers = sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]
        for user_id in OWNER:
            SUDOERS.add(user_id)
            if user_id not in sudoers:
                sudoers.append(user_id)
                sudoersdb.update_one(
                    {"sudo": "sudo"},
                    {"$set": {"sudoers": sudoers}},
                    upsert=True,
                )
        if sudoers:
            for x in sudoers:
                SUDOERS.add(x)
    LOGGER(__name__).info(f"𝗦𝘂𝗱𝗼𝗲𝗿𝘀 𝗟𝗼𝗮𝗱𝗲𝗱...")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"𝗛𝗲𝗿𝗼𝗸𝘂 𝗔𝗽𝗽 𝗖𝗼𝗻𝗳𝗶𝗴𝘂𝗿𝗲𝗱")
            except BaseException:
                LOGGER(__name__).warning(
                    f"Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
                )
