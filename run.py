import sys
import os
import time
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Menu | Coin's Tool")
black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"

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
      1. Coin's Nuker
      2. Coin's Selfbot
      3. Coin's Nitro Generator (promocodes)
{cyan}      4. Quit{white}
      """)
    try:
        opt = int(input())
    except Exception as e:
        if type(e)==ValueError:
            print("Please enter a number!")
            time.sleep(.5)
            opt=""
            pass
            menu()
        else:
            print(e)
            opt=""
            time.sleep(.5)
            pass
            menu()
    if( opt!= 1 and opt!=2 and opt!=3 and opt !=4):
        print("Please enter a valid number!")
    if( opt!= 1 and opt!=2 and opt!=3):
        print("Please enter a valid option!")
        time.sleep(.5)
        opt=""
        menu()
    return opt

def nuker():
    os.system("python3 nuker.py || py nuker.py || python nuker.py")

def sb():
    os.system("python3 sb.py || py sb.py || python sb.py")

def nitro():
    os.system("python3 nuker.py || py nuker.py || python nuker.py")

option = menu()
while option=="":
    option = menu()

if option == 1:
    nuker()
if option == 2:
    sb()
if option == 3:
    nitro()
if option == 4:
    sys.exit()