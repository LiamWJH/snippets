import os
import shutil
import getpass
import argparse
from colorama import init, Fore, Back, Style

init(autoreset=True)

argparser = argparse.ArgumentParser()
argparser.add_argument("--showsnips", action="store_true")
argparser.add_argument("--showsnip", type=str, default=None)
argparser.add_argument("--snip", type=str, default=None)
argparser.add_argument("--delsnip", type=str, default=None)

args = argparser.parse_args()

osusername = getpass.getuser()
userfilepath = os.path.join(os.environ["APPDATA"], "Snippets")

#make folder to store snippets if it does not exist
if os.path.exists(userfilepath):
    pass
else:
    os.mkdir(userfilepath)

#main
if args.showsnips == True:
    colors = [Back.RED, Back.MAGENTA, Back.YELLOW, Back.GREEN, Back.CYAN, Back.BLUE]

    coloridx = 0
    for file in os.listdir(userfilepath):
        print(colors[coloridx] + file[:-4])

        if coloridx < 5:
            coloridx += 1
        else:
            coloridx = 0

if args.showsnip != None:
    with open(os.path.join(userfilepath, args.showsnip + ".txt"), "r") as f:
        print(Back.BLACK + Fore.YELLOW + f.read() + Style.RESET_ALL)

if args.snip != None:
    filedata = ''
    filename = ''
    with open(os.path.join(os.getcwd(),args.snip), "r") as f:
        filedata = f.read()
        filename = input("Choose snippet name: ") + ".txt"
        
    with open(os.path.join(userfilepath, filename), "w") as f:
        f.write(filedata)
if args.delsnip != None:
    filename = args.delsnip
        
    os.remove(os.path.join(userfilepath, filename + ".txt"))