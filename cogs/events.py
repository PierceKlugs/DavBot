import discord
from discord import channel
from discord import client
from discord.ext import commands
import time
from discord.message import Message
import requests


class Events(discord.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @client.event()
    async def on_ready(self):
        channel = self.bot.get_channel(892118314933948456)
        weatherurl = requests.get(
            f"https://api.weather.gov/points/35.4393,-88.6418").json()
        #channel = self.bot.get_channel(892118314933948456)
        forecast = requests.get(weatherurl["properties"]["forecast"]).json()[
            "properties"]
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

def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
