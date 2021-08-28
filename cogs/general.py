import discord
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands import bot
from discord import Embed


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
    async def helps(self, ctx: commands.Context):
        await ctx.author.send(f"```yaml\nDavBot | Commands\n=================================\n$assist - Notifies Moderators and Owners you need assistance.\n\n$links - Dav sends you a message with all class links.\n\n$legendary <NAME OF PROFESSOR> - Displays a GIF of a Professor (Options: casey,scott,nichols)\n\n$SI <OPTION> - Will do SI commands (Options: schedule, assist)\n\n```")

    @commands.command()
    async def poll(self, ctx: commands.Context, *question):
        poll_item = Embed(title = f"{' '.join(question)}", description = "DavBot Polls!\nRespond to the poll by pressing the thumbs up or down!", colour=Color.from_rgb(255, 61, 61))
        poll_item.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwaterview.org%2Fwp-content%2Fuploads%2F2018%2F12%2Fdavid-shannon.jpg&f=1&nofb=1")
        poll_item.set_footer(text=f"Polled by {ctx.author.name}")
        sent_message = await ctx.send(embed=poll_item)
        await sent_message.add_reaction("👍")
        await sent_message.add_reaction("👎")
        
        #poll_embed = discord.Embed(title = f"{question}", description = "Respond down below:")
        #sent_message = await ctx.send(embed = poll_embed)
        #await sent_message.add_reaction("🇽")
        #await sent_message.add_reaction("✅")


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))