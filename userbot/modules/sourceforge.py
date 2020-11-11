# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#© ElytrA8

import asyncio
import time
from userbot import CMD_HELP
from userbot.events import register


@register(pattern="^.sf ?(.+?|) (?:)(sftp)")
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Transfer in Progress")
    PROCESS_RUN_TIME = 1000
    input_str = event.pattern_match.group(1)
    selected_transfer = event.pattern_match.group(2)
    if input_str:
        file_name = input_str
    else:
        reply = await event.get_reply_message()
        file_name = await bot.download_media(reply.media, Var.TEMP_DOWNLOAD_DIRECTORY)
    event.message.id
    CMD_WEB = {
     "sftp": "expect -c " 
              spawn sftp $SFUSER\
              expect \"yes/no\"\
              send \"yes\r\"\
              expect \"Password\"\
              send \"$::env(SFPASS)\r\"\
              expect \"sftp> \"\
              send \"$::env(SFDIR)\r\"\
              set timeout -1\
              send \"put \"{}\"\r\"\
              expect \"Uploading\"\
              expect \"100%\"\
              expect \"sftp>\"\
              \ninteract""}
    try:
        selected_one = CMD_WEB[selected_transfer].format(file_name)
    except KeyError:
        await event.edit("Error")
    cmd = selected_one
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    await event.edit(f"{stdout.decode()}")
CMD_HELP.update({"sourceforge":
                 "`.sf` (filepath) `sftp`"})
