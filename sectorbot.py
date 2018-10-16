import discord
from discord.ext import commands
import sys, traceback
import logging
import os

logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix=";")

@bot.command()
@commands.is_owner()
async def die(ctx):
    await ctx.send("Bot is shutting down.")
    await bot.logout()
    print("\nBot has shut down.")

@bot.listen()
async def on_ready():

    print(f'\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    
    init_status = discord.Status.online
    init_game = discord.Game(name='Project Name Here')
    await bot.change_presence(status=init_status, activity=init_game)

    print(f'Successfully logged in and booted...!')

@bot.command()
async def hi(ctx):
    await ctx.send('hello')

bot.run(os.environ['token'], bot=True, reconnect=True)
