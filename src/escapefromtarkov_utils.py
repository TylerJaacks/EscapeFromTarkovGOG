from galaxy.api.consts import LicenseType, Platform
from galaxy.api.types import LicenseInfo, Game

platform = Platform("Escape from Tarkov")
game = Game('escapefromtarkov', 'Escape from Tarkov', None, LicenseInfo(LicenseType.SinglePurchase))


def game_is_owned():
    return True


def launch_game():
    print("Launching game!")
