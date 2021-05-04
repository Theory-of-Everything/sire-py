# This file is reycled code from an older project, for now its a placeholder


import discord
from discord.ext import commands
import random
class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Fun Module is Online.")
    
    # Commands
    @commands.command(name="yeet", help="Makes a weird noise.")
    async def yeet_command(self, ctx):
        quotes = ["yeet", "yoot", "YEET", "YOOT", "yap"]
        response = random.choice(quotes)
        await ctx.send(response)

def setup(client):
    client.add_cog(Fun(client))
