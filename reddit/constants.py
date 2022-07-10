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
CUTE = ["cute", "Awww", "babyduckgifs", "rarepuppers", "cutecats"]
DUCK = ["duck", "babyduckgifs"]
FERRETS = ["ferret", "ferrets", "FerretsGoneWild"]
MEMES = ["dankmemes", "memes"]
PHOTOS = ["Nikon", "streetphotography", "analog", "photographs", "mobilephotography",
    "itookapicture", "wildlifephotography", "astrophotography", "retouching", "birdpics",
    "Astronomy", "LandscapePhotography", "pics", "urbanexploration", "japanpics",
    "foodphotography", "blackandwhite", "fashionphotography", "shootingcars", "nightphotography",
    "AbstractPhotos", "macro", "earthporn"]
WALLPAPERS = ["wallpaper", "iphonewallpapers", "MinimalWallpaper", "topwalls",
    "WQHD_Wallpaper", "iWallpaper", "WidescreenWallpaper"]

# Art Subreddits
CONCEPT = ["imaginaryaetherpunk", "imaginarycityscapes", "imaginarycolorscapes", "imaginarymindscapes", "art",
    "smypatheticmonsters", "conceptart"]
CHARACTER = ["imaginarycharacters", "characterart", "characterdrawing", "dndart"]
PIXEL = ["pixelart", "pixelartwallpapers", "animatedpixelart"]

MAIN = [CUTE, DUCK, FERRETS, MEMES, PHOTOS, WALLPAPERS]
ART = [CONCEPT, CHARACTER, PIXEL]

# NSFW Subreddits
FOUR_K = ["Hegre", "HighResASS", "HighResNSFW", "NSFW_Wallpaper", "UHDnsfw"]
AHEGAO = ["AhegaoGirls", "EyeRollOrgasm", "O_Faces", "RealAhegao", "ahegao"]
ASS = ["AssOnTheGlass", "AssReveal", "AssholeBehindThong", "ButtsAndBareFeet", "GodBooty",
    "HighResASS", "HungryButts", "Mooning", "SnakeButt", "TheUnderbun",
    "Upshorts", "ass", "assinthong", "asstastic", "beautifulbutt",
    "bigasses", "booty", "brunetteass", "datgap", "girlsinleggings",
    "girlsinyogapants", "hugeass", "paag", "pawg", "facedownassup", "bigblackasses"]
ANAL = ["AnalGW", "MasterOfAnal", "NotInThePussy", "anal",
    "analinsertions", "assholegonewild", "buttsthatgrip"]
BBW = ["BBW", "BBW_Chubby", "GoneWildPlus", "PerkyChubby",
    "chubby", "gonewildcurvy"]
BDSM = ["BDSMGW", "BDSM_NoSpam", "Bondage", "Spanking", "bdsm", "ropeart"]
BLOWJOB = ["AsianBlowjobs", "Blowjobs", "OralCreampie", "SwordSwallowers",
    "blowjobsandwich", "AmateurDeepthroat", "DeepthroatTears", "deepthroat"]
BOOBS = ["AreolasGW", "BestTits", "BigBoobsGW", "BigBoobsGonewild", "BiggerThanYouThought",
    "Boobies", "BoobsBetweenArms", "BustyNaturals", "BustyPetite", "Nipples",
    "PerfectTits", "PiercedNSFW", "Stacked", "TheHangingBoobs", "TheUnderboob",
    "TinyTits", "Titties", "TittyDrop", "bigboobs", "boobbounce", "boobgifs",
    "boobs", "burstingout", "fortyfivefiftyfive", "ghostnipples", "homegrowntits",
    "hugeboobs", "naturaltitties", "pokies", "smallboobs", "tits"]
BOTTOMLESS = ["Bottomless", "nopanties", "upskirt"]
COSPLAY = ["CosplayBoobs", "CosplayLewd", "gwcosplay", "nsfwcosplay"]
CUNNI = ["CunnilingusSelfie", "cunnilingus"]
CUMSHOTS = ["GirlsFinishingTheJob", "amateurcumsluts", "bodyshots", "cumfetish", "cumontongue",
    "cumshots", "facialcumshots", "pulsatingcumshots", "unexpectedcum"]
DICK = ["penis", "cock", "bulges", "twinks", "ThickDick", "MassiveCock", "Blackdick",
    "blackcock", "bigblackcocks"]
DOUBLE_P = ["Techical_DP", "doublepenetration"]
FEET = ["ButtsAndBareFeet", "Feet_NSFW", "Feetup", "FootFetish", "legsup", "rule34feet"]
FEMDOM = ["Femdom", "femdom", "hentaifemdom"]
FUTA = ["FutanariHentai", "Rule34_Futanari", "cutefutanari"]
GAY = ["CuteGuyButts", "GayGifs", "ManSex", "NSFW_GAY", "broslikeus", "bulges",
    "gaybears", "gaynsfw", "gayotters", "jockstraps", "ladybonersgw"]
GROUPS = ["GroupOfNudeGirls", "groupsex"]
LESBIANS = ["HDLesbianGifs", "Lesbian_gifs", "StraightGirlsPlaying", "girlskissing",
    "amateurlesbians", "lesbians", "mmgirls", "scissoring"]
MILF = ["AgedBeauty", "HotAsianMilfs", "blackmilfs", "obsf", "MILFs", "Milfie",
    "amateur_milfs", "cougars", "maturemilf", "milf"]
PUBLIC = ["ChangingRooms", "Flashing", "FlashingAndFlaunting", "FlashingGirls",
    "NSFW_Outdoors", "NotSafeForNature", "NudeInPublic", "PublicFlashing", "WoodNymphs",
    "bitchinbubba", "casualnudity", "exposedinpublic", "girlsflashing", "gwpublic",
    "holdthemoan", "publicplug", "snowgirls"]
PUSSY = ["GodPussy", "Innies", "LabiaGW", "LipsThatGrip", "MoundofVenus", "PerfectPussies",
    "PussyFlashing", "PussyMound", "grool", "legsup", "peachlips", "pelfie", "pussy",
    "rearpussy", "spreadeagle", "ButterflyWings", "DangleAndJingle"]
REAL_GIRLS = ["RealGirls", "Nude_Selfie", "EbonyGirls", "ebonyamateurs"]
RULE_34 = ["Rule_34", "WesternHentai", "rule34", "rule34cartoons", "rule34_ass",
    "Rule34Overwatch", "Overwatch_Porn", "Rule34LoL", "2booty", "ecchi",
    "animeecchigifs", "animenudefilters", "doujinshi", "dvansfw",
    "ecchigifs", "dota2smut", "fitdrawngirls", "healsluts", "hentaimanga",
    "imaginaryboners", "pantsu", "sukebei", "waifusgonewild", "wholesomehentai"]
THIGHS = ["ThickThighs", "Thigh", "datgap", "leggingsgonewild", "legs",
    "legsup", "theratio", "thighhighs"]
TRANS = ["GoneWildTrans"]
WILD = ["ArtGW", "AsiansGoneWild", "BigBoobsGW", "BigBoobsGonewild", "GWCouples",
    "GWNerdy", "GirlsWithBikes", "GoneWildSmiles", "LingerieGW", "PetiteGoneWild",
    "Swingersgw", "TallGoneWild", "UnderwearGW", "altgonewild", "bigonewild",
    "dirtysmall", "gonewild", "gonewildcolor", "gonewildcouples", "gonewildcurvy",
    "gwpublic", "librarygirls", "workgonewild"]
YIFF = ["Hyiff", "Yiffbondage", "femyiff", "yiff", "yiffgif"]

NSFW = [FOUR_K, AHEGAO, ASS, ANAL, BBW, BDSM, BLOWJOB, BOOBS, BOTTOMLESS, COSPLAY, CUNNI, CUMSHOTS,
    DICK, DOUBLE_P, FEET, FEMDOM, FUTA, GAY, GROUPS, LESBIANS, MILF, PUBLIC, PUSSY, REAL_GIRLS,
    RULE_34, THIGHS, TRANS, WILD, YIFF]
