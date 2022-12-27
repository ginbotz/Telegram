import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "16051908")
    API_HASH = getenv("API_HASH", "abf9b83f9ca40cf9f5ba9bf6e6afaa8b")
    TOKEN = getenv("TOKEN", "5705099329:AAHn8d1ggv7jIreU4Ha8Sljp1EW_9N_xByg")
    OWNER_ID = getenv("OWNER_ID", "5307865914")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "5581544044")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOJYBu2b7eEuusbz5bHFngg5RP95HIz-9xL52-tkxNCaUEodk0eMWjjCw8sk-HSjOkCaz7cNoH2mpryQTn0dJ3yS3kuV2A5huaT40MclSgNlVk2bjcySfdNzjt5NxvrO8KPR9bsSHosZf-ngv1VJTE6W_Ju8IdVRARXeN3PPJVNKmcxNBO9Eqwzbq9cF08zmU_EyGISGxGcWl8rsPjEvWSwNOGOg8iri3euZ5fLKeU4S4NRUdsAsoUjCJoOFelR8hKhExT3KB2uT3Cj7ibR8vX1nK8c1QcP_SfOIQEWcV7iFDhsWU5dcmx3SgfQ698wUouAd3qjNN-Fpj8MCaMCGyKr3vHBE=") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "SexyAaditya")
    DB_URI = getenv("DATABASE_URL", "mongodb+srv://starxrobo:starxrobo@cluster0.efstcnr.mongodb.net/?retryWrites=true&w=majority")
    DB_URI = DB_URI.replace("postgres", "postgres://wyuztsqv:3215xfPpCJTjTMlq9wRHL8j-Zo-lt70w@batyr.db.elephantsql.com/wyuztsqv")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001842160008")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001842160008")
    SYS_ADMIN = getenv("SYS_ADMIN", "5307865914")
    DEV_USERS = getenv("DEV_USERS", "5171357677")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "TH3ONLYCHANNEL")
    SUPPORT = getenv("SUPPORT", "TH3ONLYSUPPORT")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/0e20f2832a8a845dd9c2f.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/0e20f2832a8a845dd9c2f.jpg")
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5171357677").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "5171357677").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
