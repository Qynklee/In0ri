from telegram import Bot
from datetime import datetime

CHAT_ID = "bar"
TOKEN = "foo"
bot = Bot(TOKEN)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


def sendBot(url, img_path):
    bot.sendPhoto(
        CHAT_ID,
        photo=open(img_path, "rb"),
        caption="⚠️" + "Website " + url + " was defaced!\n" + "At " + current_time,
    )
