#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("20462802", default=None, cast=int)
API_HASH = config("dd98d5b8a57cf65d450b746a9c9052af", default=None)
BOT_TOKEN = config("5625785348:AAEqTOnCUFEVjDqg0ws4XghXH9odoHo5t6M", default=None)
SESSION = config("BQCspFYVybNYwVSsV033CINE2f85Ng49rYnBKjw-QwQ3HZQ1ZImL7Tqrvwfa4VSg4roRoiJp-1V1DPiJP1MSQs6Hfq4i5Kam8wXtJdFl8TxhSk28UqkCIf76IdWAVpmBG03GMstK97RJ67gUfoqip662r54vsz-jaj1eiw8uftHrTS4yEpNJ6zWuW155FIYhoCpl1Ic0KwPg_YYB5lD3lx6yrPHVmwqJMM29a2ocX114p8jLS1dxW6r5mR8q5H2fNgSeihtCLMmFq4hXGDVOGI9pABz2XP52lnKokkHZD73LCYqUTM-x5s8cprFJCSBZs9v3QFNRlXgPV_wevp9F-zPlAAAAAUq9VukA", default=None)
FORCESUB = config("-1001468992261", default=None)
AUTH = config("5548889833", default=None, cast=int)

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
