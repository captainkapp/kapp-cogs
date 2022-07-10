import asyncio
import concurrent

import discord
from redbot.core import checks, commands

class kapptools(commands.Cog):
    "A bunch of useful commands and utilities."

    __author__ = "Kapp"
    __version__ = "1.0.0"

    # Avatar
    @commands.command()
    async def avatar(self, ctx, *, user: discord.Member=None):
        "Provides user avatar URL."

        author = ctx.author

        if not user:
            user = author
        
        if user.is_avatar_animated():
            url = user.avatar_url_as(format="gif")
        if not user.is_avatar_animated():
            url = user.avatar_url_as(static_format="png")
        
        await ctx.send("{}'s Avatar URL : {}".format(user.name, url))