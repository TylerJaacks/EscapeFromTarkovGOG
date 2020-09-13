import requests
import os

from src import registry_util

ESCAPE_FROM_TARKOV_DOWNLOAD_URL = 'https://prod.escapefromtarkov.com/launcher/download'
ESCAPE_FROM_TARKOV_FILENAME = "%TEMP%/BsgLauncherLatest.exe"


def download_game():
    request = requests.get(ESCAPE_FROM_TARKOV_DOWNLOAD_URL, allow_redirects=True)

    open(ESCAPE_FROM_TARKOV_FILENAME, 'wb').write(request.content)


def install_game():
    if not is_installed():
        print("Escape from Tarkov is being installed.")
        download_game()
        os.system(ESCAPE_FROM_TARKOV_FILENAME)
    else:
        print("Escape from Tarkov is already installed.")


def uninstall_game():
    if not is_installed():
        print("Uninstalling Escape from Tarkov!")
    else:
        print("Escape from Tarkov is not installed.")


def is_installed():
    return True
