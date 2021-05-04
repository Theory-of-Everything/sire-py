# More Placeholder content for a future module 


import discord
from discord.ext import commands

class Fetch(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Fetch Module is Online.")
    
    

def setup(client):
    client.add_cog(Utilities(client))