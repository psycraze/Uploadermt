import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = os.environ.get("AUTH_USERS", "")
    # reg: Procedures
    UTUBE_BOT_USERS = AUTH_USERS
    SUPER_DLBOT_USERS = AUTH_USERS
    SUPER3X_DLBOT_USERS = AUTH_USERS
    SUPER7X_DLBOT_USERS = AUTH_USERS
    BANNED_USERS = os.environ.get("BANNED_USERS", "")
    # Wat was I thinking? :\
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 0
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # for storing the user details
    DB_SQLALCHEMY = "USERS.session"
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = os.environ.get("OUO_IO_API_KEY", "msSBfnhq")
    #mirro
    MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY", "")
    #mirror
    MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_TOKEN", "")
    # for Google Custom Search Engine
    GCS_API_KEY = os.environ.get("GCS_API_KEY", None)
    GCS_SE_ID = os.environ.get("GCS_SE_ID", None)
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # dict to hold Google Drive SignIns
    G_DRIVE_AUTH_DRQ = {}
