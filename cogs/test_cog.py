# This cog is for testing

import discord
from discord.ext import commands


class Resources(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Resources Module is Online.")

    @commands.command(name="embed", help="Creates a simple embed")
    async def embed(self, ctx, title: str = "Title", desc: str = "Hello World!"):
        print("Assembling Embed")
        embed = discord.Embed(title=title, description=desc, color=discord.Color.default())
        embed.add_field(name="Field 1", value="hi", inline=False)
        embed.set_image(url="https://discordpy.readthedocs.io/en/latest/_images/snake.png")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Resources(client))
