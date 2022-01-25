import discord
from discord import channel
from discord.ext import commands


class SI(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    #The SI command is a command designated as a tool for an SI in Computer Science
    async def SI(self, ctx: commands.Context, arg1: str):
        si_channels = [782127136655671316]
        si_id = 131420748823789568

        #Prints out the SI Schedule
        #WARNING: Change the schedule based off the school year
        if (arg1 == "schedule"):
            #Schedule File
            schedule_file = open("./schedule/schedule.txt")
            schedule_lines = schedule_file.readlines()
            schedule = ""
            for line in schedule_lines:
                schedule += line


            #Send out Schedule
            if(ctx.author.id == si_id):
                for si_channel in si_channels:
                    await self.bot.get_channel(si_channel).send(schedule)
            else:
                await ctx.author.send(schedule)
            
        
        #Alerts the SI that a user needs assistance
        #WARNING: Change the IDs according to the school year
        elif (arg1 == "assist" and ctx.channel.id in si_channel):
            assist = f"<@{ctx.author.id}>"
            await ctx.send(f"<@131420748823789568>, {assist} is in need of assistance.")
        
        #Alerts all students that the SI session has been cancelled, for CIS172
        #WARNING: Change the IDs according to the school year
        elif (arg1 == "cancel" and ctx.author.id == si_id):
            for si_channel in si_channels:
                    await self.bot.get_channel(si_channel).send(f"@here, <@{si_id}> has cancelled the SI meeting for today...")



def setup(bot: commands.Bot):
    bot.add_cog(SI(bot))

    