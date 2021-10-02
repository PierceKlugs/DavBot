import discord
from discord.ext import commands


class SI(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    #The SI command is a command designated as a tool for an SI in Computer Science
    async def SI(self, ctx: commands.Context, arg1: str):
        
        #Prints out the SI Schedule
        #WARNING: Change the schedule based off the school year
        if (arg1 == "schedule" and ctx.channel.id == 877927229382881290 or ctx.channel.id == 877963775746134106):
            await ctx.send("```\nOffice Hours:\nTuesday: 7:00pm - 8:00pm\nWednesday: 8:00pm - 9:00pm\n\nSI Sessions:\nMonday/Thursday: 7:00pm - 8:00pm\n```")
        
        #Alerts the SI that a user needs assistance
        #WARNING: Change the IDs according to the school year
        elif (arg1 == "assist" and ctx.channel.id == 877927229382881290 or ctx.channel.id == 877963775746134106):
            assist = f"<@{ctx.author.id}>"
            await ctx.send(f"<@131420748823789568>, {assist} is in need of assistance.")
        
        #Alerts all students that the SI session has been cancelled, for CIS172
        #WARNING: Change the IDs according to the school year
        elif (arg1 == "cancel" and ctx.channel.id == 877927229382881290 or ctx.channel.id == 877963775746134106 and ctx.author.id == 131420748823789568):
            await ctx.send(f"<@877253774056501309> <@877254044907876373>, <@131420748823789568> has cancelled the SI meeting for today...")


def setup(bot: commands.Bot):
    bot.add_cog(SI(bot))

    