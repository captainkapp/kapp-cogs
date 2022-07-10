from .kapptools import kapptools

def setup(bot):
    bot.add_cog(kapptools(bot))