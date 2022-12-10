#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 1963061
API_HASH = "99fa8ea44969f3555a0bf39452ed55a6"
BOT_TOKEN = "5633340009:AAGwP6vCzS9-lHEGb6mOGF1Ek-shyQNt_4g"
SESSION = "BQA_VCvdhes7BRuh-RuK0DF_xSzmWeaExQRXBiHGgX1RtiQQPg7jq09NoAgY6iJqJqhHZ9LlbtI-I0ZXpYrNQp8jfOjArCc48bgk3umKpFIHZmhmkhPcdy4zoJv_AtVcBTmw5WPXi_4cyQTlRBcYuechke6borEcYAA_VY55JOpyrsMiWf-Oqzj6oDjamW5wgVnbxB76IFX10viDIbn4Qx3YHbeK1XZcYAoBAcigMTfjPPFsh5JSq6W9Qj-ECN24ZVhavErI_kH0FLvdwelb-H4gQhgm8SrOpjIDPKFSNIj5TPdKhSdxvklQ_wu9VeQJFIsWf5Od77ug1vhAjPts0TAdEmF7eAA"
FORCESUB = "myttindo"
AUTH = 5548889833, 308378488

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
