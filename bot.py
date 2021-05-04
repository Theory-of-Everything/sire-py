
# Aisaka Bot
# Created by Theory_of_Everything
# A Bot Designed for the Code pit Discord server. The scorce is on Github if anyone is interested

import os
import discord
from discord.ext import commands, tasks
from decouple import config # Required for Enviroment Variables
import random
from itertools import cycle

#* Client Varibles
TOKEN = config('TOKEN') # Grab Token from the .env file
SERVER_INFO = config('SERVER_INFO')
client = commands.Bot(command_prefix="]") #* Note there is a space after the ]

#* other variables
status_dot_cycle = cycle([discord.Status.online, discord.Status.dnd])

# events
@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(activity=discord.Game(" with fireflies"))
    print(f"{client.user.name} has connected to Discord!")

@client.event # general error handler
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter all valid arguments to the command!")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command!")

# command for loading modules
@client.command()
async def loadModule(ctx, module):
    client.load_extension(f"cogs.{module}")
    ctx.send(f"{module} was loaded.")
# command for unloading modules
@client.command()
async def unloadModule(ctx, module):
    client.load_extension(f"cogs.{module}")
    ctx.send(f"{module} was unloaded.")

@client.command()
async def about(ctx):
    embed = discord.Embed(title="bot@theoryware", Description="Github Repo", color=discord.Color.green(), url="https://github.com/Theory-of-Everything/Aisaka-Bot")
    embed.add_field(name="About Me", value="I am a utility bot Desgined specifically for managing small tech-oriented comminutes.\n\n I am Currently in the very early stages of my development, \n but that doesn't mean I wont go far!", inline=False)
    embed.add_field(name="Host Information", value=SERVER_INFO, inline=False)
    embed.add_field(name="Other info", value="made with discord.py", inline=False)
    embed.set_footer(text="Made by Theory_of_Everything#4163", icon_url="https://cdn.discordapp.com/avatars/356953662297473025/52bf1495980dfe60520a3a6a7cd9b4a7.png?size=128")
    await ctx.send(embed=embed)

@client.command()
async def contrib(ctx):
    embed = discord.Embed(title="Contribute to Development", color=discord.Color.green())
    embed.add_field(name="How to Contribute", value="If you can contribute to the bots development, please do, either in the discord or the github repository", inline=False)
    embed.set_footer(text="Made by Theory_of_Everything#4163", icon_url="https://cdn.discordapp.com/avatars/356953662297473025/52bf1495980dfe60520a3a6a7cd9b4a7.png?size=128")
    await ctx.send(embed=embed)



# tasks
@tasks.loop(seconds=2)
async def change_status():
    await client.change_presence(activity=discord.Game(" with fireflies"), status=next(status_dot_cycle))

# cog loading initializer
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
