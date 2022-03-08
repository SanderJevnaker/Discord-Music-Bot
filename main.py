import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix="?", intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

#Enter token from the Discord bot website
client.run("OTIyODgzMjI1ODg4NjQxMDI0.YcH7-w._d6tSkMDI6HUigavdMdfhZkW8BY")