# Scrap Mechanic Mod Tracer
Ever gotten a "Failed to build shape" error message while trying to load a Scrap Mechanic creation?
Some workshop creations don't tell you what mods you need.
You may have uninstalled a mod needed by your creations.
With the Scrap Mechanic Mod Tracer, you can figure out which mods are needed by creations.

# Installation
## The easy way
Grab the [latest release](https://github.com/git4o/scrap-mod-trace/releases/tag/latest) and run  main.exe.
> [!IMPORTANT]
> It is highly recommended to place the exe file in a dedicated folder, as it will create a .env file so it can remember your game's install directory.


## The hard way
You can grab the main python file from the repo
Install the requirements with `pip install -r requirements.txt`

# How to use
The script will take you through choosing your Scrap Mechanic save file dir and its workshop folder.
Then, press 1 or 2 depending on if you want it to search downloaded workshop creations or your own creations.
> [!NOTE]
> If you have installed Scrap Mechanic to somewhere other than the default location i.e. an external drive, the workshop folder will be under: `<Your other steam library>\steamapps\workshop`.
> For example, I have Scrap Mechanic installed on my F: Driver under the SteamLibrary library name and my path looks like:
> `F:\SteamLibrary\steamapps\workshop`

# Troubleshooting
If the program crashes, or does not show a creation, make sure you typed the first word correctly and look closely at the console after you enter the name.
If you see an error message displayed briefly, rename your creation and make sure it does not include any single (') or double (") quotes or any unicode symbols in the name.
If your creation has an invalid name, as described above, you can rename it in Scrap Mechanic and it should work.
The program should be able to handle these, but issues do sometimes arise.

If the program does not detect a mod that is needed by the creation, some mods that are not made very well may improperly declare their presence in the creation and there is no consistent way to fix this, but in testing, the script works 97% of the time.


