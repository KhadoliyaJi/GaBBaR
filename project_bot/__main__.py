import glob



from pathlib import Path

from project_bot.utils import load_plug
import logging
from . import tgbot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

path = "project_bot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        pxt = Path(a.name)
        plugg = pxt.stem
        load_plug(plugg.replace(".py", ""))

print("GaBBaR bot has Started & loaded all plugins")

if __name__ == '__main__':
    tgbot.run_until_disconnected()