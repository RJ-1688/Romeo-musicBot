import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from Romeo.utilities import config
from Romeo.utilities.config.config import BANNED_USERS
from Romeo import app, bot, LOGGER
from Romeo.modules.core.call import main
from Romeo.plugins import ALL_MODULES
from Romeo.modules.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Romeo").error(
            "š„ ššØ šš¬š¬š¢š¬š­šš§š­ šš„š¢šš§š­š¬ [ššš«š¬] ššØš®š§šā"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("ššØš¦ššØ").warning(
            "š„ ššØ šš©šØš­š¢šš² ššš«š¬ šššš¢š§ššā...\nš· ššØš®š« ššØš­ ššØš§'š­ šš ššš„š ššØ šš„šš² šš©šØš­š¢šš² šš®šš«š¢šš¬ā..."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await bot.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Romeo.plugins" + all_module)
    LOGGER("Romeo.modules.plugins").info(
        "š„ šš®ššš¬š¬šš®š„š„š² šš¦š©šØš«š­šš šš„š„ ššØšš®š„šš¬ šæ "
    )
    await app.start()
    await main.start()
    try:
        await main.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("ššØš¦ššØ").error(
            "[šš«š«šØš«] - \n\nš„ šš„ššš¬š šš®š«š§ šš§ ššØš¢šš šš”šš­ šš ššØš®š« ššØš š šš« šš«šØš®š©ā..."
        )
        sys.exit()
    except:
        pass
    await main.decorators()
    LOGGER("ššØš¦ššØ").info("š„³ ššØš§š š«šš­š®š„šš­š¢šØš§š¬, ššØš®š« ššØš­ šš®šššš¬š¬šš®š„š„š² ššš©š„šØš²šš āØ...")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Romeo").info("š šš²š¬š­šš¦ šš­šØš©š©šš, ššØšØššš²šā...")
