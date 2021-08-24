import discord
from discord import client
from discord.client import Client
from discord.ext import commands
from discord.ext.commands import bot

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def assist(self, ctx: commands.Context):
        await ctx.send(f"<@803348026420232263>, {ctx.author} is in need of assistance.")

    @commands.command()
    async def legendary(self, ctx: commands.Context, name: str):
        
        if name == "casey":
            await ctx.channel.send(file = discord.File("gifs/casey.gif"))
        elif name == "scott":
            await ctx.channel.send(file = discord.File("gifs/scott.gif"))
        elif name == "nichols":
            await ctx.channel.send("Coming Soon...")

    @commands.command()
    async def links(self, ctx: commands.Context):
        await ctx.author.send(f"Canvas: https://fhu.instructure.com/login/canvas \nGoogle Classroom: https://classroom.google.com/u/0/h \nGitHub: https://github.com/ \nVisual Studio Code: https://code.visualstudio.com/ \nPython: https://www.python.org/downloads/")

    @commands.command()
    async def commands(self, ctx: commands.Context):
        await ctx.author.send(f"```yaml\nDavBot | Commands\n=================================\n$assist - Notifies Moderators and Owners you need assistance.\n\n$links - Dav sends you a message with all class links.\n\n$legendary <NAME OF PROFESSOR> - Displays a GIF of a Professor (Options: casey,scott,nichols)\n\n$SI <OPTION> - Will do SI commands (Options: schedule, assist)\n\n```")


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))