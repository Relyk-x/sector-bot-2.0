import discord
from discord.ext import commands
import os
import sys, traceback

logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix=";")
# cog importing
cogs = ["cog one", "cog two"]

if __name__ == '__main__':
    for cog in cogs:
        try:
            bot.load_extension(f'cog.{cog}')
            print(f"Successfully loaded {cog}")
        except Exception as e:
            print(f'Failed to load cog {cog}. --', file=sys.stderr)
            traceback.print_exc()

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


bot.run(os.environ['token'], bot=True, reconnect=True)
