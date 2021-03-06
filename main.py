# 10 May 2022
# Author: Novoos https://t.me/novoosecosystem
# Python 3.10.4


import datetime
import redis
from os import getenv
from pyrogram import Client, filters
from dotenv import load_dotenv
import asyncio
import logging
logging.basicConfig(level=logging.INFO)


load_dotenv('config.env')



API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION = getenv("SESSION")
REDIS_URI = getenv("REDIS_URI")
REDIS_PASSWORD = getenv("REDIS_PASSWORD")
REDIS_URL = str(REDIS_URI).split(":")[0]
REDIS_PORT = str(REDIS_URI).split(":")[1]


r = redis.Redis(
    host=REDIS_URL,
    port=REDIS_PORT, 
    password=REDIS_PASSWORD)


app = Client(name="NoovosAFKBot",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)


def is_afk():
    if str(r.get(name="AFK"),"UTF-8")=="True":
        return True
    else:
        return False


def get_reason():
    reason = str(r.get(name="REASON"),"UTF-8")
    return reason


def set_reason(reason):
    r.set(name="REASON",value=reason)


@app.on_message(filters.me & filters.regex('^.afk'))
async def set_afk(client, message):
    global start_time
    reason = message.text.replace('.afk', """""").strip()
    r.set(name="AFK",value="True")
    set_reason(reason=reason)
    start_time = datetime.datetime.now()
    await message.edit(f"__Going AFK__\n__Reason: {reason}__\n\n__Made with ❤️ by__\n**__@NovoosEcosystem__**")
    await asyncio.sleep(2)
    await message.delete()


@app.on_message(filters.me & filters.text)
async def disable(client, message):
    r.set(name="AFK", value="False")


@app.on_message(filters.private)
async def afk(client, message):
    if is_afk():
        reason = get_reason()
        finished_time = datetime.datetime.now()
        total_afk_time = finished_time - start_time
        time = int(total_afk_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        elif h > 0:
            endtime += f"{h}h {m}m {s}s"
        else:
            endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
        await message.reply(f"Hello **{message.chat.first_name}**,\n\n**__Currently I am not available__**\n\n**Reason**: {reason} \n\nLast Seen: {endtime} ago \n\n**__Made with ❤️ by__**\n**__@NovoosEcosystem__** ")


app.run()
