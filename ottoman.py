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
   
@client.command()
async def embed(ctx):
    embed = discord.Embed(title="DENEME",description="DENEME")
    embed.add_field(name="DENEME",value="DENEME")
    embed.add_field(name="DENEME",value="DENEME")
    embed.set_image(url="[İMAGE URL]")
    embed.set_thumbnail(url="[İMAGE URL]")
    embed.set_footer(text="DENEME BOT")
    await ctx.send(embed=embed)
  
token = "[TOKEN]"
client.run(token)
