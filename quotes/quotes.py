from random import randrange

from redbot.core import commands
from redbot.core.data_manager import bundled_data_path

class Quotes(commands.Cog):
    """Says a random quote from a predetermined list."""

    @commands.command()
    async def quote(self, ctx):
        "Says a random quote."

        filepath = bundled_data_path(self) / "lines.txt"
        with filepath.open() as file:
            line = next(file)
            for num, readline in enumerate(file):
                if randrange(num + 2):
                    continue
                line = readline
        await ctx.maybe_send_embed(line)
