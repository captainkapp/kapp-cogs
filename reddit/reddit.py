import discord

from redbot.core import commands
from redbot.core.i18n import Translator, cog_i18n

import contextlib

from . import constants as sub
from .core import Core

_ = Translator("reddit", __file__)

@cog_i18n(_)
class reddit(Core):
    """Send random images from subreddits."""

    # NSFW Commands
    @commands.command(aliases=["butt", "booty"])
    async def ass(self, ctx):
        """Sends an ass image from a random subreddit."""

        await self._send_msg(ctx, _("ass"), sub.ASS)
    
    # SFW Commands
    @commands.command(aliases=["meme", "dank"])
    async def memes(self, ctx):
        """Sends a meme from a random subreddit."""

        await self._send_msg(ctx, _("memes"), sub.MEMES)

    @commands.command(aliases=["vintage"])
    async def retro(self, ctx):
        """Sends a retro image from a random subreddit."""

        await self._send_msg(ctx, _("retro"), sub.RETRO)