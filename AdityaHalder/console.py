import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", ,"27271850"))
API_HASH = getenv("API_HASH", "5757fd61c4bd95d7021ab6d8445fa4db")
BOT_TOKEN = getenv("BOT_TOKEN", "6720409081:AAGAS9qGJpJ3z0Cqv4RrF3mLHLgnrvZIoM0")
STRING_SESSION = getenv("STRING_SESSION", "BQGgIqoAGrvcEWVLZx_R2TvEuTq5-AGBH_YLMOQPvj43-UEPAdrPbfH8Cs-AFGHRc3lQ1usotVNhSJtMoAbT3Fkw5tdqC2fe5bpXEcbV-MacYWPExkTXGuAc6_12tjTCKQi2MK4cpSHlw8d1GhtlPLzfkwM9gawlMJOdndN2NTiKK5mGY60f_rEtTiDAjd0kh_9kD_0E2FVbd3RDf7-wFCkv7E0TqcAyX2I8wwV9uCqwKEYZvXew3nJ32BQp0bILrzVQoGDYcjMeqVUHsGPXoxgcXOnJpz7r2vJjvlk4_OOfpvE3x2nT-DEspPU-Zg_PGIF6JLFsH8Vv4zqNLqrFyb923t7bVQAAAAGaZt-4AA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://minhazan990:minhaz@cluster0.r2okalv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1001842764318))


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 Hey, I am an advanced & superfast high quality userbot assistant with an upgraded version security system.\n\n🌿 I can't let you message my owner's dm without my owner's permission.\n\n🌺 My owner is offline now, please wait until my owner allows you.\n\n🍂 Please don't spam here, because spamming will force me to block you from my owner id.**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))



# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://graph.org/file/1f543761e199a754b3f21.mp4")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("Genius")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

