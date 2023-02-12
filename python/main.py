#!/usr/bin/env python3

# REQ: Creates HTML5 color roles. <skr>

from discord import Intents
from discord import Game
from discord import Colour
from discord.ext.commands import Bot
from os import environ
from webcolors import CSS3_NAMES_TO_HEX

PREFIX = '!'

INTENTS = Intents.default()
INTENTS.message_content = True

GAME= Game(name="musical notes 🎶")

BOT = Bot(command_prefix=PREFIX, intents=INTENTS, activity=GAME)

NAME = 'sing'
ALIASES = [
  'punk',
  'rock'
]

@BOT.command(aliases=ALIASES)
async def sing(context):
    print(context)
    for name, hex in CSS3_NAMES_TO_HEX.items(): 
        hex_color = Colour.from_str(hex)

        role_opts = {
          'name': name,
          'color': hex_color,
        }

        await context.send(f'{name}:{hex}')
        await context.guild.create_role(**role_opts)

TOKEN = environ['DISCORD_TOKEN']

BOT.run(TOKEN)