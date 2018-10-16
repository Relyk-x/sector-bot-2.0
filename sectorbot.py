import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=";")

@bot.listen()
async def on_ready():
    print("Ready for use!")

@bot.listen()
async def hi (ctx):
    await ctx.send ("Hello") 

bot.run(os.environ['token'])
