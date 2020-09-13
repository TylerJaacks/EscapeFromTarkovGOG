# Galaxy plugin for Escape from Tarkov 

This plugin allows you to install and launch your Escape from Tarkov via the GOG Galaxy 2.0 launcher.

## Installation
Use build-in `Search` engine from GOG Galaxy 2.0 Settings

*Note: This code is based on https://github.com/bartok765/galaxy_blizzard_plugin*

### Installing from source
- copy / clone this repo
- run:
```bash
cd EscapeFromTarkov
pip install -r requirements/dev.txt
inv install
```

## Uninstallation (remove all data)
Click `Disconnect` button in GOG Galaxy Settings. If you see `Connect` instead of `Disconnect` (this may happen on plugin crash or accessing from different machine) you need to connect it again and then disconnect.

### "Soft" disconnect (advanced)
If you want to keep imported data (owned games, play time), but do not need to sync more and play with local games, you can "turn off" local plugin:
- close Galaxy
- remove plugin local database (on Windows usually at `C:\ProgramData\GOG.com\Galaxy\storage\plugins`).

## Help us finding Classic Blizzard Games

If you have classic Blizzard games which are not properly detected as installed or don't launch when clicking 'play'
please provide the name and values of the games key under

```
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\
```

Windows registry path (by opening `Run`-> `regedit`)

If on MAC please provide the games bundle_id which can be found by calling

```
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -dump | grep {game_name}
```

## Development

Install required packages for building and testing:

```bash
pip install -r requirements/dev.txt
```

You may want to install the pacakges in a virtual environment:

```bash
pip install virtualenv
cd galaxy_blizzard_plugin
virtualenv .venv
.venv\Scripts\activate.bat
pip install -r requirements/dev.txt
```

Run tests:
```bash
inv test
```

Build package
```bash
inv build [--output=<output_folder>] [--ziparchive=<zip_package_name.zip>]
```

#### Shortcuts:

Build to local plugins folder
```bash
inv install
```

Build zip package with name indicating current version:
```bash
inv pack
```