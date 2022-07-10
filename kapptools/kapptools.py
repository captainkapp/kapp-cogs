import asyncio
import concurrent

import discord
import speedtest-cli
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

    # Speedtest
    @commands.command()
    async def speedtest(self, ctx):
        "Test internet speed of the bot's host server."
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        loop = asyncio.get_event_loop()
        speed_test = speedtest.Speedtest(secure=True)
        the_embed = await ctx.send(
            embed=self.generate_embed(0, speed_test.results.dict())
        )
        await loop.run_in_executor(executor, speed_test.get_servers)
        await loop.run_in_executor(executor, speed_test.get_best_server)
        await the_embed.edit(embed=self.generate_embed(1, speed_test.results.dict()))
        await loop.run_in_executor(executor, speed_test.download)
        await the_embed.edit(embed=self.generate_embed(2, speed_test.results.dict()))
        await loop.run_in_executor(executor, speed_test.upload)
        await the_embed.edit(embed=self.generate_embed(3, speed_test.results.dict()))
    
    @staticmethod
    def generate_embed(step: int, results_dict):
        """Generate the embed."""
        measuring = ":mag: Measuring..."
        waiting = ":hourglass: Waiting..."

        color = discord.Color.red()
        title = "Measuring internet speed..."
        message_ping = measuring
        message_down = waiting
        message_up = waiting
        if step > 0:
            message_ping = f"**{results_dict['ping']}** ms"
            message_down = measuring
        if step > 1:
            message_down = f"**{results_dict['download'] / 1_000_000:.2f}** mbps"
            message_up = measuring
        if step > 2:
            message_up = f"**{results_dict['upload'] / 1_000_000:.2f}** mbps"
            title = "Speedtest Results"
            color = discord.Color.green()
        embed = discord.Embed(title=title, color=color)
        embed.add_field(name="Ping", value=message_ping)
        embed.add_field(name="Download", value=message_down)
        embed.add_field(name="Upload", value=message_up)
        return embed