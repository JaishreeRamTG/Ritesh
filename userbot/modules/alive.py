thunder = "thunder"
Thunder = "thunder"
borg = "borg"

"""Check if thundert alive"""
# CREDITS: @WhySooSerious, @Sur_vivor
import time

from uniborg.util import thunder_on_cmd, sudo_cmd

from userbot import ALIVE_NAME, Lastupdate
from userbot.Configs import Config
from userbot.modules import currentversion


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = Config.ALIVE_IMAGE
pm_caption = "➥ **𝕿𝖍𝖚𝖓𝖉𝖊𝖗 IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.9.0` \n"
pm_caption += f"➥ **Uptime** : `{uptime}` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `{currentversion}`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/Anmol-dot283/Thunder/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [Anmol-dot283@Github](GitHub.com/Anmol-dot283)\n"
pm_caption += "➥ **Check Stats By Doing** `.stat`. \n\n"
pm_caption += "[🇮🇳 Deploy 𝕿𝖍𝖚𝖓𝖉𝖊𝖗Userbot 🇮🇳](https://telegra.ph/Thunder-06-15)"


@Thunder.on(thunder_on_cmd(pattern=r"alive"))
@Thunder.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def Thunder(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()