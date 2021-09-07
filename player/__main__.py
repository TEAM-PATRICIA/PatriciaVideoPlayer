import sys
import glob
import asyncio
import importlib
from pathlib import Path
from pytgcalls import idle
from player import Bot, UB, group_calls
from player.config import Var
from player.modules import player
loop = asyncio.get_event_loop()

_path = f"player/modules/*.py"
files = glob.glob(_path)

def load_plugins(plugin_name):
    path = Path(f"player/modules/{plugin_name}.py")
    name = "player.modules.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(load)
    sys.modules[f"player.modules." + plugin_name] = load
    print("Imported => " + plugin_name)

async def client_start(bot=False):
    print('\n')
    print('------------------- Initalizing VC BOT ---------------------')
    # Assistant bot
    if bot:
        await Bot.start()
    await UB.start()
    await group_calls.start()
    print('----------------------- DONE ------------------------')
    print('--------------------- Importing ---------------------')
    for name in files:
        with open(name) as a:
            path_ = Path(a.name)
            plugin_name = path_.stem
            load_plugins(plugin_name.replace(".py", ""))
    print('----------------------- INITIATED VIDEO PLAYER BOT ------------------------')
    print('             Logged in as User =>> {}'.format((await UB.get_me()).first_name))
    if bot:
        print('             and Bot =>> {}'.format((await Bot.get_me()).first_name))
    print('-----------------------------------------------------')

if __name__ == '__main__':
    is_bot = bool(Var.BOT_TOKEN)
    loop.run_until_complete(client_start(bot=is_bot))
idle()
