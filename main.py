import discord
from cogs import *
import os
from discord.ext import commands
from discord.ext.commands.core import Command

#Important Variables

si_id = "<@131420748823789568>"
cis172 = "<@806916153255133184>"
bot = commands.Bot(command_prefix="$")
bot.remove_command('help')
#Load all Cogs
bot.load_extension("cogs.si")
bot.load_extension("cogs.general")

#Start Up
@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

#Token and Run
token = open("C:/Users/Admin/Desktop/Token/token.txt").readlines()[0]
bot.run(f'{token}')