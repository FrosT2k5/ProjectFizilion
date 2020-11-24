from telethon import events
import random, re
from userbot import CMD_HELP
import asyncio 
from userbot.events import register


@register(outgoing=True, pattern="^.fun$")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Oh My God!😂")
        await asyncio.sleep(1.0)
        await event.edit("That's the funniest Joke I've ever heard🤣")
        await asyncio.sleep(1.5)
        await event.edit("I can't stop Laughing🤣")
        await asyncio.sleep(1.0)
        await event.edit("I can't stop Laughing!🤣")
        await asyncio.sleep(1.0)
        await event.edit("Okay, That was the Worst Joke I've ever Heard")
        await asyncio.sleep(1.9)
        await event.edit("I just Laughed so that you don't feel bad😶")
