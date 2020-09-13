import sys
from abc import ABC
from typing import Any, List, Dict, Union, Optional

from galaxy.api.consts import LocalGameState, Platform
from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.types import Achievement, Game, LicenseInfo, LocalGame, GameTime, LicenseType

from src import (
    escapefromtarkov_utils,
    installer_utils
)

version = "1.0"

is_owned = False
is_installed = False


class EscapeFromTarkovPlugin(Plugin, ABC):
    def __int__(self, reader, writer, token):
        super().__init__(escapefromtarkov_utils.platform, version, reader, writer, token)

        self.is_owned = escapefromtarkov_utils.game_is_owned()
        self.is_installed = installer_utils.is_installed()

    async def get_owned_games(self) -> List[Game]:
        if is_owned:
            print("Escape from Tarkov is owned!")
            return [escapefromtarkov_utils.game]
        else:
            return []

        pass

    async def launch_game(self, game_id: str) -> None:
        if is_owned:
            if is_installed:
                print("Launching Escape from Tarkov!")
                escapefromtarkov_utils.launch_game()
            else:
                print("Escape from Tarkov is not installed!")
        else:
            print("You don't own Escape from Tarkov!")

        pass

    async def install_game(self, game_id: str) -> None:
        if is_owned and not is_installed:
            print("Escape from Tarkov is being installed!")
            installer_utils.install_game()
        else:
            print("You either don't own Escape from Tarkov or the game is already installed.")

        pass

    async def uninstall_game(self, game_id: str) -> None:
        if is_installed:
            print("Escape from Tarkov is being uninstalled!")
            installer_utils.uninstall_game()
        else:
            print("Escape from Tarkov is not currently installed.")

        pass


def main():
    create_and_run_plugin(EscapeFromTarkovPlugin, sys.argv)


if __name__ == "__main__":
    main()
