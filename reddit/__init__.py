from redbot.core.bot import Red
from .reddit import reddit

def setup(bot: Red):
    cog = reddit(bot)
    bot.add_cog(cog)