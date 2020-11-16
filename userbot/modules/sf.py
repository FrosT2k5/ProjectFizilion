from userbot import CMD_HELP, SFUSER, SFPASS, SFDIR
from userbot.events import register
import pexpect
import os

@register(outgoing=True, pattern=r"^\.sf (.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Uploading To SourceForge")
    filepath = event.pattern_match.group(1)
    if input:
        filepath = input
    else:
        reply = await event.get_reply_message()
        filepath = await bot.download_media(reply.media, Var.TEMP_DOWNLOAD_DIRECTORY)

sf = pexpect.spawn ('sftp SFUSER@frs.sourceforge.net')
sf.expect ('yes/no')
sf.sendline ('yes')
sf.expect ('Password:')
sf.sendline ('SFPASS')
sf.expect ('sftp> ')
sf.sendline ('cd SFDIR')
sf.expect ('sftp> ')
sf.sendline ('put format.(filepath)')
sf.expect ('Uploading*')
sf.expect ('100%')
sf.expect ('sftp> ')
sf.sendline ('bye')
os.remove(.ssh/known_hosts)
event.edit("Done Uploading")
