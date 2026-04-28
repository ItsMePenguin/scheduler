import discord
import os
from discord.ext import commands

client=  commands.Bot(command_prefix='!', intents=discord.Intents.all())



@client.event
async def on_ready():
    print(f"{client.user} is now online!")
    await client.tree.sync()

@client.event
async def on_message(message):  
    if message.author == client.user:
        return

@client.tree.command(name="command")
async def say(interaction: discord.Interaction):
    await interaction.response.send_message(message)
        

# client.run( token here )
