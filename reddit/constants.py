from random import choice

def emoji():
    """Randomize footer emojis."""
    EMOJIS = [
        "\N{AUBERGINE}",
        "\N{SMIRKING FACE}",
        "\N{PEACH}",
        "\N{SPLASHING SWEAT SYMBOL}",
        "\N{BANANA}",
        "\N{KISS MARK}",
    ]
    emoji = choice(EMOJIS)
    return emoji

REDDIT_BASEURL = "https://api.reddit.com/r/{sub}/random"
MARTINE_API_BASE_URL = "https://api.martinebot.com/v1/images/subreddit"
IMGUR_LINKS = ("http://imgur.com", "https://m.imgur.com", "https://imgur.com")
NOT_EMBED_DOMAINS = ("gfycat.com/", "gifdeliverynetwork.com/", "redgifs.com", "imgur.com/gallery/", "imgur.com/a/", ".gifv")
GOOD_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", "gifv")

# Main Subreddits
MEMES = ["dankmemes", "memes"]
RETRO = ["oldschoolcool", "thewaywewere"]

# NSFW Subreddits
FOUR_K = ["Hegre", "HighResASS", "HighResNSFW", "NSFW_Wallpaper", "UHDnsfw"]
AHEGAO = ["AhegaoGirls", "EyeRollOrgasm", "O_Faces", "RealAhegao", "ahegao"]
ASS = ["AssOnTheGlass", "AssReveal", "AssholeBehindThong", "ButtsAndBareFeet", "GodBooty",
    "HighResASS", "HungryButts", "Mooning", "SnakeButt", "TheUnderbun",
    "Upshorts", "ass", "assinthong", "asstastic", "beautifulbutt",
    "bigasses", "booty", "brunetteass", "datgap", "girlsinleggings",
    "girlsinyogapants", "hugeass", "paag", "pawg", "facedownassup"]
# ANAL
# BBW
# BDSM
# BLOWJOB
# BOOBS
# BOTTOMLESS
# COSPLAY
# CUNNI
# CUMSHOTS
# DEEPTHROAT
# DICK
# EBONY
# FACIALS
# FEET
# FEMDOM
# FUTA
# GAY
GROUPS = ["GroupOfNudeGirls", "groupsex"]
# LESBIANS
# MILF
# ORAL
# PUBLIC
# PUSSY
# REAL_GIRLS
# REDHEADS
RULE_34 = ["Rule_34", "WesternHentai", "rule34", "rule34cartoons", "rule34_ass",
    "Rule34Overwatch", "Overwatch_Porn", "Rule34LoL"]
# SQUIRT
THIGHS = ["ThickThighs", "Thigh", "datgap", "leggingsgonewild", "legs",
    "legsup", "theratio", "thighhighs"]
# THREESOME
TRANS = ["GoneWildTrans"]
WILD = ["ArtGW", "AsiansGoneWild", "BigBoobsGW", "BigBoobsGonewild", "GWCouples",
    "GWNerdy", "GirlsWithBikes", "GoneWildSmiles", "LingerieGW", "PetiteGoneWild",
    "Swingersgw", "TallGoneWild", "UnderwearGW", "altgonewild", "bigonewild",
    "dirtysmall", "gonewild", "gonewildcolor", "gonewildcouples", "gonewildcurvy",
    "gwpublic", "librarygirls", "workgonewild"]
YIFF = ["Hyiff", "Yiffbondage", "femyiff", "yiff", "yiffgif"]
