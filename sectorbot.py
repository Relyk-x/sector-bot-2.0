import discord
from discord.ext import commands

token = 'NTAxNjg3MTUyNTE0NDMzMDI1.DqdBHQ.hTbxEAp1oPlBTw_aRiAS7hrRrRQ'
bot = commands.Bot(command_prefix=";")

@bot.event
async def on_ready():
	print("Ready for use!")

client.run(os.getenv('token'))
