import discord
from discord.ext import commands
import asyncio
client = commands.Bot(command_prefix="!") #BOT PREFİX

@client.event
async def on_ready():
    print("BOT ONLİNE")
    client.change_presence(activity=discord.Game(name="DENEME ONLİNE"))


@client.command()
async def deneme(ctx):
    await ctx.send("DENEME")

token = "[TOKEN]"
client.run(token)