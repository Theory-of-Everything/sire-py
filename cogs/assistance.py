import discord
from discord.ext import commands

class Assistance(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Assistance Module is Online")

    #* General Assistance Commands
    @commands.command(name="codehelp", help="Displays Links for General Code Help")
    async def codehelp(self, ctx):
        embed = discord.Embed(name="General Code Help", description="Some good rescorces for help with programming", color=discord.Color.blue())
        embed.add_field(name="r/learnprogramming", value="https://www.reddit.com/r/learnprogramming/", inline=False)
        embed.add_field(name="Stack Overflow", value="https://stackoverflow.com/questions", inline=False)
        await ctx.send(embed=embed)


    
    #* C# Language Commands

    @commands.command(name="csharphelp", help="Shows Help pages For the C# language.")
    async def csharphelp(self, ctx):
        embed = discord.Embed(name="C# Help", description="Some good rescorces for help with c#", color=discord.Color.blue())
        embed.add_field(name="Microsoft C# Docs", value="https://docs.microsoft.com/en-us/dotnet/csharp/", inline=False)
        embed.add_field(name="w3schools page", value="https://www.w3schools.com/cs/default.asp", inline=False)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/C_Sharp_logo.svg/1200px-C_Sharp_logo.svg.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Assistance(client))