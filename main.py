import discord
from cogs import *
import os
from discord.ext import commands
from discord.ext.commands.core import Command
import requests
import time

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
    channel = bot.get_channel(892118314933948456)
    weatherurl = requests.get(
    f"https://api.weather.gov/points/35.4393,-88.6418").json()
        #channel = self.bot.get_channel(892118314933948456)
    forecast = requests.get(weatherurl["properties"]["forecast"]).json()["properties"]
    while True:
        # channel.send(f"{weatherurl.json()}")
        times = forecast["periods"]
        message = ""

        # Temperature Info
        period = None
        temperature = 0
        windspeed = 0
        shortforecast = ""
        detailedforecast = ""

        # Print
        for i in times:
            period = i["name"]
            temperature = i["temperature"]
            windspeed = i["windSpeed"]
            shortforecast = i["shortForecast"]
            detailedforecast = i["detailedForecast"]
            message = f"```WEATHER\n============================\nTime: {period}\nTemperature: {temperature}\nWindspeed: {windspeed}\n```"
            channel.send(f"{message}")
        time.sleep(86400)


#Token and Run
token = open("./Token/token.txt").readlines()[0]
bot.run(f'{token}')