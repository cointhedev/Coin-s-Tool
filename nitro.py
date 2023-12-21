#im lazy to add proxies (not just bc i dont have any)
import sys
import os
import time
import json
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

if config['pyorpython'] == 'py':
    python = False
    py = True
else:
    python = True
    py = False

if config['path'] == 'y':
    path = True
else:
    path = False

if path == True:
    os.system("pip install threads")
    os.system("pip install httpx")
else:
    if python:
        os.system("python -m pip install threads")
        os.system("python -m pip install httpx")   
    if py:
        os.system("py -m pip install threads")
        os.system("py -m pip install httpx")

black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"
os.system("cls")
print(f"""{red}
 $$$$$$\            $$\         $$\                                           
$$  __$$\           \__|        $  |                                          
$$ /  \__| $$$$$$\  $$\ $$$$$$$\\_/$$$$$$$\                                   
$$ |      $$  __$$\ $$ |$$  __$$\ $$  _____|                                  
$$ |      $$ /  $$ |$$ |$$ |  $$ |\$$$$$$\                                    
$$ |  $$\ $$ |  $$ |$$ |$$ |  $$ | \____$$\                                   
\$$$$$$  |\$$$$$$  |$$ |$$ |  $$ |$$$$$$$  |                                  
 \______/  \______/ \__|\__|  \__|\_______/                                   
                                                                              
                                                                              
                                                                              
$$\   $$\ $$\   $$\                                                           
$$$\  $$ |\__|  $$ |                                                          
$$$$\ $$ |$$\ $$$$$$\    $$$$$$\   $$$$$$\                                    
$$ $$\$$ |$$ |\_$$  _|  $$  __$$\ $$  __$$\                                   
$$ \$$$$ |$$ |  $$ |    $$ |  \__|$$ /  $$ |                                  
$$ |\$$$ |$$ |  $$ |$$\ $$ |      $$ |  $$ |                                  
$$ | \$$ |$$ |  \$$$$  |$$ |      \$$$$$$  |                                  
\__|  \__|\__|   \____/ \__|       \______/                                   
                                                                              
                                                                              
                                                                              
 $$$$$$\                                                    $$\               
$$  __$$\                                                   $$ |              
$$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\ $$$$$$\    $$$$$$\  
$$ |$$$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \____$$\\_$$  _|  $$  __$$\ 
$$ |\_$$ |$$$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|$$$$$$$ | $$ |    $$ /  $$ |
$$ |  $$ |$$   ____|$$ |  $$ |$$   ____|$$ |     $$  __$$ | $$ |$$\ $$ |  $$ |
\$$$$$$  |\$$$$$$$\ $$ |  $$ |\$$$$$$$\ $$ |     \$$$$$$$ | \$$$$  |\$$$$$$  |
 \______/  \_______|\__|  \__| \_______|\__|      \_______|  \____/  \______/ 
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
 $$$$$$\                                                                      
$$  __$$\                                                                     
$$ |  \__|                                                                    
$$ |                                                                          
$$ |                                                                          
\__|                                                                               {white}
""")
import httpx
import uuid
import random
import threading
ratelimit = False
def gen():
    global ratelimit
    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    headers = {
        "Content-Type": "application/json",
        "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
    }
    data = {
        "partnerUserId": str(uuid.uuid4())
   }
    response = httpx.post(url,json=data,headers=headers,timeout=5)
    if response.status_code == 200:
        token = response.json().get('token')
        if token:
            link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
            with open("promos.txt", "a") as f:
                f.write(f"{link}\n")
            print("Succesfully generated promo link: {}".format(link))
            ratelimit=False
    elif response.status_code == 429:
        print(f"rate limit")
        ratelimit = True
    else:
        print("failed {} | content: {}".format(response.status_code,response.content))

#fuck ratelimit!
while True:
    threading.Thread(target=gen).start()
