import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def assist(self, ctx: commands.Context):
        await f"<@803348026420232263>, {ctx.author} is in need of assistance."

    @commands.command()
    async def legendary(self, ctx: commands.Context, name: str):
        
        if name == "casey":
            await ctx.channel.send(file = discord.File("gifs/casey.gif"))
        elif name == "scott":
            await ctx.channel.send(file = discord.File("gifs/scott.gif"))
        elif name == "nichols":
            await ctx.channel.send("Coming Soon...")

def setup(bot: commands.Bot):
    bot.add_cog(General(bot))