# This file is reycled code from an older project, for now its a placeholder


import discord
from discord.ext import commands
import random
class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Utilities Module is Online.")
    
    # Commands
    @commands.command(name="stats", help="Generates stats based off user input")
    async def stats(self, ctx, health: int, attack: int, defense: int):
        stat_health = health
        stat_attack = attack
        stat_defense = defense
        await ctx.send(f"Stats Generated! The stats are {stat_health} health, {stat_attack} attack, and {stat_defense} defense.")

    @commands.command(name="roll", help="Rolls a random number based on a user defined range and number of rolls.\nThe result is sent as a message.")
    async def roll_command(self, ctx, roll_range: int, number_of_rolls: int):
        dice = [str(random.choice(range(1, roll_range + 1))) for _ in range(number_of_rolls)]
        await ctx.send("You Rolled: " + ", ".join(dice))

def setup(client):
    client.add_cog(Utilities(client))