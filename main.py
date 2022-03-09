import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix="?", intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

#Discord bot token
client.run("OTIyODgzMjI1ODg4NjQxMDI0.YcH7-w.dQ5ItDn_Ysl56qZOgfTZ8-TyIag")