import os
import time
import sys

black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"
def nuker():
    os.system("py nuker.py || python3 nuker.py || python nuker.py")

def sb():
    os.system("py sb.py || python3 sb.py || python sb.py")

def nitro():
    os.system("py nitro.py || python3 nitro.py || python nireo.py")
def menu():
    while True:
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
        1. Coin's Nuker{white}
{cyan}        2. Coin's Selfbot{white}
{blue}        3. Coin's Nitro Generator (promocodes){white}
{cyan}        4. Quit{white}
        """)
        try:
            opt = int(input())
        except Exception as e:
            if type(e)==ValueError:
                print(f"{red}Please enter a number!{white}")
                time.sleep(.5)
                continue
            else:
                print(red+str(e)+white)
                time.sleep(.5)
                continue
        if opt!= 1 and opt!=2 and opt!=3 and opt !=4:
            print(f"{red}Please enter a valid option!{white}")
            time.sleep(.5)
            continue
        else:
            break
    return opt

option = menu()
if option == 1:
    nuker()
if option == 2:
    sb()
if option == 3:
    nitro()
if option == 4:
    sys.exit()
