import os
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger



from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession

from .Config import Config

StartTime = time.time()
catversion = "2.10.6"


CAT_ID = ["1035034432", "551290198"]

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="[%(asctime)s]- %(name)s- %(levelname)s- %(message)s",
        level=INFO,
        datefmt="%m-%d %H:%M:%S",
    )
LOGS = getLogger(__name__)




# Global Configiables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}

if Config.STRING_SESSION:
    session_name = str(Config.STRING_SESSION)
    try:
        if session_name.endswith("="):
            bot = TelegramClient(
                StringSession(session_name), Config.APP_ID, Config.API_HASH
            )
        else:
            bot = TelegramClient(
                "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.STRING_SESSION)
    except Exception as e:
        LOGS.warn(f"STRING_SESSION - {str(e)}")
        sys.exit()
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Config.APP_ID, Config.API_HASH)
