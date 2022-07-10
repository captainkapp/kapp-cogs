import discord

from redbot.core import commands
from redbot.core.i18n import Translator, cog_i18n

import contextlib

from . import constants as sub
from .core import Core

_ = Translator("reddit", __file__)

@cog_i18n(_)
class reddit(Core):
    """Send random images from random subreddits."""

    # Group Subreddit Commands
    @commands.command()
    async def mainrandom(self, ctx):
        """Sends a random image from the main subreddits."""

        await self._send_msg(ctx, _("main random"), sub.MAIN)
    
    @commands.command()
    async def artrandom(self, ctx):
        """Sends a random image from the art subreddits."""

        await self._send_msg(ctx, _("art random"), sub.ART)

    @commands.command()
    async def nsfwrandom(self, ctx):
        """Sends a random image from the NSFW subreddits."""

        await self._send_msg(ctx, _("nsfw random"), sub.NSFW)

    # Main Subreddit Commands
    @commands.command()
    async def cute(self, ctx):
        """Sends a cute image from a random subreddit."""

        await self._send_msg(ctx, _("cute"), sub.CUTE)

    @commands.command()
    async def duck(self, ctx):
        """Sends a duck image from a random subreddit."""

        await self._send_msg(ctx, _("duck"), sub.DUCK)

    @commands.command()
    async def ferrets(self, ctx):
        """Sends a ferret image from a random subreddit."""

        await self._send_msg(ctx, _("ferrets"), sub.FERRETS)

    @commands.command(aliases=["meme", "dank"])
    async def memes(self, ctx):
        """Sends a meme from a random subreddit."""

        await self._send_msg(ctx, _("memes"), sub.MEMES)

    @commands.command()
    async def photos(self, ctx):
        """Sends an image from a random photography subreddit."""

        await self._send_msg(ctx, _("photos"), sub.PHOTOS)

    @commands.command()
    async def wallpapers(self, ctx):
        """Sends a wallpaper from a random subreddit."""

        await self._send_msg(ctx, _("wallpapers"), sub.WALLPAPERS)

    # Art Subreddit Commands
    @commands.command()
    async def concept(self, ctx):
        """Sends concept art from a random subreddit."""

        await self._send_msg(ctx, _("concept"), sub.CONCEPT)

    @commands.command()
    async def character(self, ctx):
        """Sends character art from a random subreddit."""

        await self._send_msg(ctx, _("character"), sub.CHARACTER)

    @commands.command()
    async def pixel(self, ctx):
        """Sends pixel art from a random subreddit."""

        await self._send_msg(ctx, _("pixel"), sub.PIXEL)

    # NSFW Subreddit Commands
    @commands.command(name=["4k"], aliases=["4K"])
    async def four_k(self, ctx):
        """Sends a 4k image from a random subreddit."""

        await self._send_msg(ctx, _("4k"), sub.FOUR_K)

    @commands.command()
    async def ahegao(self, ctx):
        """Sends an ahegao image from a random subreddit."""

        await self._send_msg(ctx, _("ahegao"), sub.AHEGAO)

    @commands.command(aliases=["butt", "booty"])
    async def ass(self, ctx):
        """Sends an ass image from a random subreddit."""

        await self._send_msg(ctx, _("ass"), sub.ASS)

    @commands.command()
    async def anal(self, ctx):
        """Sends an anal image from a random subreddit."""

        await self._send_msg(ctx, _("anal"), sub.ANAL)

    @commands.command()
    async def bbw(self, ctx):
        """Sends some bbw images."""

        await self._send_msg(ctx, _("bbw"), sub.BBW)

    @commands.command()
    async def bdsm(self, ctx):
        """Sends some bdsm from random subreddits."""

        await self._send_msg(ctx, _("bdsm"), sub.BDSM)

    @commands.command(aliases=["blowjobs", "fellatio"])
    async def blowjob(self, ctx):
        """Sends some blowjob images/gifs from random subreddits."""

        await self._send_msg(ctx, _("blowjob"), sub.BLOWJOB)

    @commands.command(aliases=["boob", "boobies", "tits", "titties", "breasts", "breast"])
    async def boobs(self, ctx):
        """Sends some boobs images from random subreddits."""

        await self._send_msg(ctx, _("boobs"), sub.BOOBS)

    @commands.command()
    async def bottomless(self, ctx):
        """Sends some bottomless images from random subreddits."""

        await self._send_msg(ctx, _("bottomless"), sub.BOTTOMLESS)

    @commands.command()
    async def cosplay(self, ctx):
        """Sends some nsfw cosplay images from random subreddits."""

        await self._send_msg(ctx, _("nsfw cosplay"), sub.COSPLAY)

    @commands.command(aliases=["cunni", "pussyeating"])
    async def cunnilingus(self, ctx):
        """Sends some cunnilingus images from random subreddits."""

        await self._send_msg(ctx, _("cunnilingus"), sub.CUNNI)

    @commands.command(aliases=["cum", "cums", "cumshots"])
    async def cumshot(self, ctx):
        """Sends some cumshot images/gifs from random subreddits."""

        await self._send_msg(ctx, _("cumshot"), sub.CUMSHOTS)

    @commands.command(aliases=["cock"])
    async def dick(self, ctx):
        """Sends some dicks images from random subreddits."""

        await self._send_msg(ctx, _("dick"), sub.DICK)

    @commands.command(aliases=["doublep"])
    async def doublepenetration(self, ctx):
        """Sends some double penetration images/gifs from random subreddits."""

        await self._send_msg(ctx, _("double penetration"), sub.DOUBLE_P)

    @commands.command()
    async def feet(self, ctx):
        """Sends some feet images from random subreddits."""

        await self._send_msg(ctx, _("feet"), sub.FEET)

    @commands.command()
    async def femdom(self, ctx):
        """Sends some femdom images from random subreddits."""

        await self._send_msg(ctx, _("femdom"), sub.FEMDOM)

    @commands.command(aliases=["futanari"])
    async def futa(self, ctx):
        """Sends some futa images from random subreddits."""

        await self._send_msg(ctx, _("futa"), sub.FUTA)

    @commands.command(aliases=["gayporn"])
    async def gay(self, ctx):
        """Sends some gay porn from random subreddits."""

        await self._send_msg(ctx, _("gay porn"), sub.GAY)

    @commands.command(aliases=["groups", "nudegroup", "nudegroups"])
    async def group(self, ctx):
        """Sends some groups nudes from random subreddits."""

        await self._send_msg(ctx, "groups nudes", sub.GROUPS)

    @commands.command(aliases=["lesbians"])
    async def lesbian(self, ctx):
        """Sends some lesbian gifs or images from random subreddits."""

        await self._send_msg(ctx, _("lesbian"), sub.LESBIANS)

    @commands.command(aliases=["milfs"])
    async def milf(self, ctx):
        """Sends some milf images from random subreddits."""

        await self._send_msg(ctx, _("milf"), sub.MILF)

    @commands.command()
    async def public(self, ctx):
        """Sends some public nude images from random subreddits."""

        await self._send_msg(ctx, _("public nude"), sub.PUBLIC)

    @commands.command(aliases=["vagina"])
    async def pussy(self, ctx):
        """Sends some pussy images from random subreddits."""

        await self._send_msg(ctx, _("pussy"), sub.PUSSY)

    @commands.command()
    async def realgirls(self, ctx):
        """Sends some real girls images from random subreddits."""

        await self._send_msg(ctx, _("real nudes"), sub.REAL_GIRLS)

    @commands.command(aliases=["r34"])
    async def rule34(self, ctx):
        """Sends some rule34 images from random subreddits."""

        await self._send_msg(ctx, _("rule34"), sub.RULE_34)

    @commands.command(aliases=["thighs", "legs"])
    async def thigh(self, ctx):
        """Sends some thighs images from random subreddits."""

        await self._send_msg(ctx, _("thigh"), sub.THIGHS)

    @commands.command()
    async def trans(self, ctx):
        """Sends some trans from random subreddits."""

        await self._send_msg(ctx, _("trans"), sub.TRANS)

    @commands.command(aliases=["wild", "gwild"])
    async def gonewild(self, ctx):
        """Sends some gonewild images from random subreddits."""

        await self._send_msg(ctx, _("gonewild"), sub.WILD)

    @commands.command(aliases=["yiffs"])
    async def yiff(self, ctx):
        """Sends some yiff images from random subreddits."""

        await self._send_msg(ctx, _("yiff"), sub.YIFF)