import json
import sys
import os
import time

black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"    
with open("config.json") as data:
    config = json.load(data)

if config['pyorpython'] == '' or config['path'] == '':
    print("Please edit the config file like so:")
    print('''
{
    "pyorpython":"", -- here put py or python, based on how u run a file py [filename].py or python [filename].py
    "path":"" --here put if u have python to path (y/n)
}''')
    sys.exit()

def menu():
    os.system("cls")
    print(f"""{red}
 $$$$$$\            $$\           $$\           
$$  __$$\           \__|          $  |          
$$ /  \__| $$$$$$\  $$\ $$$$$$$\  \_/  $$$$$$$\ 
$$ |      $$  __$$\ $$ |$$  __$$\     $$  _____|
$$ |      $$ /  $$ |$$ |$$ |  $$ |    \$$$$$$\  
$$ |  $$\ $$ |  $$ |$$ |$$ |  $$ |     \____$$\ 
\$$$$$$  |\$$$$$$  |$$ |$$ |  $$ |    $$$$$$$  |
 \______/  \______/ \__|\__|  \__|    \_______/ 
$$$$$$$$\                     $$\               
\__$$  __|                    $$ |              
   $$ |    $$$$$$\   $$$$$$\  $$ |              
   $$ |   $$  __$$\ $$  __$$\ $$ |              
   $$ |   $$ /  $$ |$$ /  $$ |$$ |              
   $$ |   $$ |  $$ |$$ |  $$ |$$ |              
   $$ |   \$$$$$$  |\$$$$$$  |$$ |              
   \__|    \______/  \______/ \__|              
{blue}
      1. Nuker
      2. Coin's Selfbot
{cyan}      3. Quit{white}
      """)
    try:
        opt = int(input())
    except Exception as e:
        if type(e)==ValueError:
            print("Please enter a number!")
            time.sleep(.5)
            pass
            menu()
        else:
            print(e)
            time.sleep(.5)
            pass
            menu()
    if( opt!= 1 and opt!=2 and opt!=3):
        print("Please enter a valid number!")
        time.sleep(.5)
        menu()
    return opt
def nuker():
    global config
    if config["pyorpython"] == 'py':
        os.system("py nuker.py")
        sys.exit()
    else:
        os.system("python nuker.py")
        sys.exit()

def sb():
    global config
    if config["pyorpython"] == 'py':
        os.system("py sb.py")
        sys.exit()
    else:
        os.system("python sb.py")
        sys.exit()

option = menu()

if option == 1:
    nuker()
if option == 2:
    sb()
if option == 3:
    sys.exit()