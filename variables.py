# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 27276412  # Get this value from my.telegram.org/apps
    API_HASH = "861593b9527c2b54d673c0dee3d8f39a"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://xlsijaoh:3OkuXNH2EysdJFfM6gxT_Z6wSepSWAap@batyr.db.elephantsql.com/xlsijaoh"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002116643591
    MESSAGE_DUMP = -1002116643591

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://sahil123:nezu2koch61n@cluster0.pvlwlz2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Support chat and support ID
    SUPPORT_CHAT = "zenitsu_bot_support"
    SUPPORT_ID = -1001997798206

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "6769807249:AAHJoA2oMBk5UUETGiIE3KHY69EfH3kqoO0"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6305653111
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = ["5603729934","5860411988","6338745050"]  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = ["6772939926"]  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
