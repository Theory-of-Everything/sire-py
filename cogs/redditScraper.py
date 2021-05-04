import os
import praw
import random
import discord
from discord.ext import commands
from decouple import config

# TODO: Upgrade from praw to Async Praw

APP_ID = config('REDDIT_APP_ID')
APP_SECRET = config('REDDIT_APP_SECRET')
# USER_AGENT = config('REDDIT_USR_AGNT')

reddit = praw.Reddit(
    client_id = APP_ID,
    client_secret = APP_SECRET,
    user_agent = "User Agent",
)

class RedditScraper(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Reddit Module is Online!")

    @commands.command()
    async def codememe(self, ctx):
        randPost = random.choice([x  for x in reddit.subreddit("ProgrammerHumor").hot(limit=100)])
        embed = discord.Embed(title=randPost.title + " from r/ProgrammerHumor", color=discord.Color.orange())
        embed.set_image(url=randPost.url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(RedditScraper(client))