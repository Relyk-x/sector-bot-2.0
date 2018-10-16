import discord
from discord.ext import commands
import sys, traceback
import logging
import os

bot = commands.Bot(command_prefix=";")

@bot.listen()
async def on_ready():
    print("Ready for use!")

@bot.command()
async def hi(ctx):
    await ctx.send('hello')

bot.run(os.environ['token'])
