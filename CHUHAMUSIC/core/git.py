#
# Copyright (C) 2024 by vishalpandeynkp1@Github, < https://github.com/vishalpandeynkp1 >.
#
# This file is part of < https://github.com/vishalpandeynkp1/CHUHAMUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/vishalpandeynkp1/CHUHAMUSIC/blob/master/LICENSE >
#
# All rights reserved.


import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config

from ..logging import LOGGER

loop = asyncio.get_event_loop_policy().get_event_loop()


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return loop.run_until_complete(install_requirements())


def git():
    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO

    try:
        repo = Repo()
        LOGGER(__name__).info(f"𝗚𝗶𝘁 𝗖𝗹𝗶𝗲𝗻𝘁 𝗙𝗼𝘂𝗻𝗱 [𝗩𝗣𝗦 𝗗𝗘𝗣𝗟𝗢𝗬𝗘𝗥]")
    except GitCommandError:
        LOGGER(__name__).info(f"Invalid Git Command")
    except InvalidGitRepositoryError:
        LOGGER(__name__).info("𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗿𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝘆, 𝗶𝗻𝗶𝘁𝗶𝗮𝗹𝗶𝘇𝗶𝗻𝗴...")
        repo = Repo.init()
        if "origin" not in repo.remotes:
            origin = repo.create_remote("origin", UPSTREAM_REPO)
        else:
            origin = repo.remote("origin")
        origin.fetch()
        repo.create_head(
            config.UPSTREAM_BRANCH,
            origin.refs[config.UPSTREAM_BRANCH],
        )
        repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
            origin.refs[config.UPSTREAM_BRANCH]
        )
        repo.heads[config.UPSTREAM_BRANCH].checkout(True)

    nrs = repo.remote("origin")
    nrs.fetch(config.UPSTREAM_BRANCH)
    try:
        nrs.pull(config.UPSTREAM_BRANCH)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    install_req("pip3 install --no-cache-dir -r requirements.txt")
    LOGGER(__name__).info(f"Fetched Updates from: {REPO_LINK}")
