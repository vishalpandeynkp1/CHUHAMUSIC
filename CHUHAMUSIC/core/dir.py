#
# Copyright (C) 2024 by vishalpandeynkp1@Github, < https://github.com/vishalpandeynkp1 >.
#
# This file is part of < https://github.com/vishalpandeynkp1/CHUHAMUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/vishalpandeynkp1/CHUHAMUSIC/blob/master/LICENSE >
#
# All rights reserved.

import logging
import os
import sys
from os import listdir, mkdir

from config import TEMP_DB_FOLDER


def dirr():
    assets_folder = "assets"
    downloads_folder = "downloads"
    cache_folder = "cache"

    if assets_folder not in listdir():
        logging.warning(
            f"{assets_folder} Folder not Found. Please clone or fork repository again."
        )
        sys.exit()

    for file in os.listdir():
        if (
            file.endswith(".jpg")
            or file.endswith(".jpeg")
            or file.endswith(".mp3")
            or file.endswith(".png")
            or file.endswith(".session")
            or file.endswith(".session-journal")
        ):
            os.remove(file)

    if downloads_folder not in listdir():
        mkdir(downloads_folder)

    if cache_folder not in listdir():
        mkdir(cache_folder)

    if TEMP_DB_FOLDER not in listdir():
        mkdir(TEMP_DB_FOLDER)

    logging.info("Directories Updated.")


if __name__ == "__main__":
    dirr()
