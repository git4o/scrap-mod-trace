import os
import json
import msvcrt
import dotenv
import tkinter as tk
import sys
from tkinter import filedialog

# load env stuff
dotenv.load_dotenv()

workdir = os.getenv('WORKDIR', '')
workshop = os.getenv('WORKSHOP', '')
appdata = os.getenv('APPDATA')
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#file dialog
def fdiag(initialdirin, titlein):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    selected_dir = filedialog.askdirectory(title=titlein, initialdir=initialdirin)
    root.destroy() 
    if selected_dir:
        return selected_dir
    else:
        print("No directory selected.")
        return None
while not workdir:
    print("Please select your game's save directory. It is usally found under C:\\Users\\<username>\\AppData\\Roaming\\Axolot Games\\Scrap Mechanic")
    input("Press enter to continue...")
    workdir = fdiag(appdata, "Select Scrap Mechanic Save Directory")
    if workdir:
        #make sure blueptint folder exist
        user_dir = os.path.join(workdir, 'User')
        if os.path.exists(user_dir):
            user_folders = [d for d in os.listdir(user_dir) if os.path.isdir(os.path.join(user_dir, d)) and d.startswith('User_')]
            if user_folders:
                workdir = os.path.join(user_dir, user_folders[0], 'Blueprints')
            else:
                print("No User folder found.")
                sys.exit(1)
                quit()
        os.environ['WORKDIR'] = workdir
        with open('.env', 'w') as f:
            f.write(f'WORKDIR={workdir}\n')
    else:
        print("Please select the Scrap Mechanic save directory.")
cls()
while not workshop:
    print("Please select your workshop directory. It is usually found under <your steam dir>\\steamapps\\workshop\nTIP! If your Scrap Mechanic Game is installed on another drive, not where Steam is installed, this workshop folder should be set to\n<Your other steam library>\\steamapps\\workshop")
    input("Press enter to continue...")
    workshop = fdiag("C:\\", "Select Scrap Mechanic Workshop Directory")
    if workshop:
        #scrap workshop dir
        workshop = os.path.join(workshop, 'content', '387990')

        if os.path.exists(workshop):
            os.environ['WORKSHOP'] = workshop
            with open('.env', 'a') as f:
                f.write(f'WORKSHOP={workshop}\n')
        else:
            print("We could not locate Scrap Mechanic in the provided workshop directory. Please check the path and try again.")
            sys.exit(1)
            quit()
    else:
        print("Please select the Scrap Mechanic workshop directory.")
cls()

#input selection using msvcrt
def print_page(page_num, items):
    cls()
    print("Page", page_num)
    start_index = (page_num - 1) * 10
    for i, (folder, name) in enumerate(items[start_index:start_index+10], start=1):
        if i == 10:
            print(f"[0] {name}")
        else:
            print(f"[{i}] {name}")
    print("Down arrow key to go to the next page, Up arrow key to go to the previous page, ESC to exit without selecting.")

def input_selection(items):
    page_num = 1
    total_pages = -(-len(items) // 10)

    print_page(page_num, items)

    while True:
        key = msvcrt.getch()
        if key == b'\x1b':  # dis is esc key
            break
        elif key.isdigit():
            index = int(key)
            if index == 0:
                index = 10
            selected_index = (page_num - 1) * 10 + index - 1
            if selected_index < len(items):
                return items[selected_index]
        elif key == b'H':  # dis is arrow up
            if page_num > 1:
                page_num -= 1
                print_page(page_num, items)
        elif key == b'P':  # arrow down
            if page_num < total_pages:
                page_num += 1
                print_page(page_num, items)

which = input("Workshop or your own creation? (1/2): ")

if which == "1":
    workdir = workshop
elif which == "2":
    workdir = workdir

search_word = input("Enter the first word of the creation to search for: ").strip().lower()

# search the name from desciptions json thingy
dirs = [d for d in os.listdir(workdir) if os.path.isdir(os.path.join(workdir, d))]
blueprints = []
for d in dirs:
    description_path = os.path.join(workdir, d, 'description.json')
    if os.path.exists(description_path):
        try:
            with open(description_path, 'r', encoding='utf-8') as f:
                description = json.load(f)
                name = description.get('name', '').lower()
                if name.startswith(search_word):
                    blueprints.append((d, name))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"Error reading {description_path}: {e}")

if blueprints:
    print("Select a blueprint to open:")
    selected_blueprint = input_selection(blueprints)
    if selected_blueprint:
        cls()
        print(f"Selected blueprint: {selected_blueprint[1]}")
        print(f"Folder: {selected_blueprint[0]}")
        
        
        blueprint_path = os.path.join(workdir, selected_blueprint[0], 'blueprint.json')
        if os.path.exists(blueprint_path):
            # extract depends
            with open(blueprint_path, 'r') as f:
                blueprint = json.load(f)
                dependencies = blueprint.get('dependencies', [])
                
                if not dependencies:
                    print("Mods already installed.")
                else:
                    dependency_names = [dep.get('name', 'Unknown') for dep in dependencies]
                    print("Dependencies:")
                    for name in dependency_names:
                        print(name)
                    
                    # missing shape uuid search
                    print("\nThat might be all the info you need, but you can narrow it down to exactly what mod is missing by searching for the ID of the shape.\n")
                    print("You can find the ID from the \"Failed to build shape\" message in the game.\n")
                    uuid_prefix = input("Enter everything up to the first '-' in the ID: ").strip().lower()
                    
                    mods = []
                    for dep in dependencies:
                        shape_ids = dep.get('shapeIds', [])
                        for shape_id in shape_ids:
                            if shape_id.startswith(uuid_prefix):
                                mods.append(dep.get('name', 'Unknown'))
                                break
                    
                    if mods:
                        print("Mods with matching shape IDs:")
                        for mod in mods:
                            print(mod)
                    else:
                        print("No mods found with matching shape IDs.")
        else:
            print("blueprint.json not found in the selected folder.")
else:
    print("No blueprints found with that word.")
input("Press enter to exit...")