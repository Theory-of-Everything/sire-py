# Author: Theory
# I have left all of the commands here a placeholders until I can fully implement Functionality

import discord
from discord.ext import commands

# TODO: Add in actual Moderation Tools and fix this section


class Modtools(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Modtools Module is Online")

    @commands.command(name="Modtest")
    async def modtest(self, ctx, member):
        await ctx.send(member)

    @commands.command(name="Kick", help="Kick a specified guild member.")
    async def kick(self, ctx):
        await ctx.send("Kick Command")
    
    @commands.command(name="Ban", help="Ban a specified guild mamber.")
    async def ban(self, ctx):
        await ctx.send("Ban Command")
    
    @commands.command(name="Mute", help="Mutes a guild member\nby assigning a muted role without \"Send Messages\" or \" Connnect to Voice Channel\" Permissons")
    async def mute(self, ctx):
        await ctx.send("Mute Command") 

def setup(client):
    client.add_cog(Modtools(client))