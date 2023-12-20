    import sys
import json
import os
with open("config.json") as data:
    config = json.load(data)
with open("sbconfig.json") as data:
    sbconfig = json.load(data)
if config['pyorpython'] == '' or config['path'] == '':
    print("Please edit the config file like so:")
    print('''
{
    "pyorpython":"", -- here put py or python, based on how u run a file py [filename].py or python [filename].py
    "path":"" --here put if u have python to path (y/n)
}''')
    sys.exit()
openaikey=""
giphyapi = ""
if sbconfig["token"] == "":
    print("Please edit the sbconfig.json file and enter your token! (OPENAI KEY AND GIPHY API KEY ARE OPTIONAL LEAVE IT BLANK)")
    sys.exit()
else:
    token = sbconfig['token']
    if sbconfig["openaikey"] != '':
        openaikey = sbconfig['openaikey']
    if sbconfig['giphyapi'] != '':
        giphyapi = sbconfig['giphyapi']
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
    os.system("pip install -r sbreq.txt")
else:
    if python:
        os.system("python -m pip uninstall py-cord -y")
        os.system("python -m pip uninstall py-cord -y")
        os.system("python -m pip uninstall discord.py -y")
        os.system("python -m pip install -r sbreq.txt") 
    if py:
        os.system("py -m pip uninstall py-cord -y")
        os.system("py -m pip uninstall py-cord -y")
        os.system("py -m pip uninstall discord.py -y")
        os.system("py -m pip install -r sbreq.txt")

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
 $$$$$$\            $$\  $$$$$$\  $$\                   $$\     
$$  __$$\           $$ |$$  __$$\ $$ |                  $$ |    
$$ /  \__| $$$$$$\  $$ |$$ /  \__|$$$$$$$\   $$$$$$\  $$$$$$\   
\$$$$$$\  $$  __$$\ $$ |$$$$\     $$  __$$\ $$  __$$\ \_$$  _|  
 \____$$\ $$$$$$$$ |$$ |$$  _|    $$ |  $$ |$$ /  $$ |  $$ |    
$$\   $$ |$$   ____|$$ |$$ |      $$ |  $$ |$$ |  $$ |  $$ |$$\ 
\$$$$$$  |\$$$$$$$\ $$ |$$ |      $$$$$$$  |\$$$$$$  |  \$$$$  |
 \______/  \_______|\__|\__|      \_______/  \______/    \____/ {white}
{blue}Prefix: >{white}""")
import discord
import openai
import httpx
from discord.ext import commands
import requests
import json
import sys
import asyncio
import random
import string
from jokeapi import Jokes
hasopenai = False
hasgiphy = False
if openaikey!="":
    openai.api_key = openaikey
    hasopenai = True
if giphyapi!="":
    hasgiphy = True
print("")
intents = discord.Intents.all()
intents.members=True
client = commands.Bot(command_prefix='>', self_bot=True,intents=intents,help_command=None,activity = discord.Game(type=discord.ActivityType.watching,name="coin.dev"))
if sbconfig["autoreply"]=="True":
    autoreply = True
    print("Autoreply is on!")
else:
    autoreply = False
    print("Autoreply is off!")

@client.event
async def on_ready():
    print("Selfbot has woken up.")

@client.event
async def on_message(message):
    global autoreply
    if autoreply == True:
        msg = message.content.lower()
        if not message.guild and message.author.id != client.user.id:
            #print(message.author.id)
            if msg == "hey" or msg =="hi" or msg == "wsp" or msg == "wsg" or msg == "yo" or msg == "hello" or msg == "wassup" or msg == "hiya" or msg =="wassup" or msg =="greetings":
                print(f"Sent no reply to {message.author.id} channel id: {message.channel.id}")
                await message.channel.send(content=f"Hey! <@{client.user.id}> will ignore your message if you just say hello. (<https://nohello.net/en>)")
    await client.process_commands(message)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,    
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]
@client.command()
async def insta_del(ctx,*,msg):
    await ctx.message.delete()
    await ctx.send(msg,delete_after=0.2)
@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    try:
        msg = await ctx.send("nuking....")
        guild = ctx.guild
        id = ctx.channel.id
        for channel in guild.text_channels:
            if channel != ctx.channel:
                try:
                    await channel.delete()
                except:
                    pass
        for channel in guild.voice_channels:
            try:
                await channel.delete()
            except:
                pass
        try:
            for channel in guild.categories:
                try:
                    await channel.delete()
                except:
                    pass
        except Exception as e:
            await ctx.respond(e)
        try:
            for role in guild.roles:
                try:
                    await role.delete()
                except:
                    pass
        except Exception as e:
            await ctx.respond(e)
            pass
        await msg.delete()
        await ctx.send("finished!",delete_after=2.5)
    except AttributeError:
        await msg.delete()
        await ctx.send("must be in a server to use this command",delete_after=2.5)
    except:
        await msg.delete()
        await ctx.send("no perms idiot",delete_after=2.5)
@client.command()
async def help(ctx):
    await ctx.message.delete()
    msg="""
```diff
-Coin's selfbot
+Help Page``````yaml
>help - displays this page
>ping - pong!
>nuke - nukes the server
>create [channel/vc] [category id] [name] - creates a channel/vc 
>category [name] - creates a category
>id [channel] - grabs the id of a channel
>kick [member] - kicks a member
>ban [member] - bans a member
>cat - returns a random cat photo
>dog - returns a random dog photo
>gif [name] - returns the first tenor gif result
>insult [member] - insults someone
>av [member] - returns the avatar of someone
>poll "[question]" "[option 1]" "[option 2]" (MUST HAVE "" OR SPACES WONT WORK) - creates a poll
>spam [ammount] [msg] - spams specified msg x times
>shutdown - the name says it 
>gay [name] - gay'o'meter
>joke - tells a joke
>eightball [message] - 8ball
>urban [word] - returns the meaning of a word using urban dict api
>run_code [code] - returns code output
>gpt [prompt] - returns chatgpt's answer
>autoreply [on/off] - turns on/off autoreply can be configured in config.json
>fact - fetches a random fact idfk lol
```
"""
    await ctx.send(msg)
@client.command()
async def autoreply(ctx,t=None):
    await ctx.message.delete()
    global autoreply
    if t!=None:
        if t=="on" or t =="off":
            if t=="on":
                autoreply = True
                await ctx.send("Autoreply turned on!",delete_after=2.5)
            else:
                autoreply = False
                await ctx.send("Autoreply turned off!",delete_after=2.5)
        else:
            await ctx.send("Invalid choice!",delete_after=2.5)
    else:
        await ctx.send("empty field",delete_after=2.5)

@client.command()
async def category(ctx,*,name:str=None):
    await ctx.message.delete()
    if name!=None:
        cat = await ctx.guild.create_category(name)
        await ctx.send(f"✅ Succesfully created category:{name}!")
    else:
        await ctx.send("No name for category!",delete_after=2.5)

@client.command()
async def id(ctx,channel:discord.TextChannel=None):
    await ctx.message.delete()
    if channel!=None:
        await ctx.send(str(channel.id))
    else:
        await ctx.send("No channel!", delete_after=2.5)

@client.command()
async def create(ctx,type,category: discord.CategoryChannel,*,name):
    await ctx.message.delete()
    print(category)
    try:
        if type.lower()!="channel" and type.lower()!="vc":
            await ctx.send("Invalid type!",delete_after=2.5)
        else:
            if category == None:
                if type.lower()=="channel":
                    channel = await ctx.guild.create_text_channel(name)
                    await ctx.send(f"Succesfully created text channel:{name} ✅")
                if type.lower()=="vc":
                    channel = await ctx.guild.create_voice_channel(name)
                    await ctx.send(f"Succesfully created voice channel:{name} ✅")
            else:
                if type.lower()=="channel":
                    channel = await category.create_text_channel(name)
                    await ctx.send(f"Succesfully created text channel:{name} ✅")
                if type.lower()=="vc":
                    channel = await category.create_voice_channel(name)
                    await ctx.send(f"Succesfully created voice channel:{name} ✅")
    except AttributeError:
        await ctx.send("must be in a server to use this command",delete_after=2.5)
    except:
        await ctx.send("no perms idiot",delete_after=2.5)
@client.command()
async def kick(ctx,member:discord.Member):
    await ctx.message.delete()
    try:
        await member.kick()
        await ctx.send(f"{member} got kicked in the ass")
    except AttributeError:
        await ctx.send("must be in a server to use this command",delete_after=2.5)
    except Exception as e:
        await ctx.send(f"no perms or member role too high ({e})",delete_after=2.5)

@client.command()
async def ban(ctx,member:discord.Member):
    await ctx.message.delete()
    try:
        await member.ban()
        await ctx.send(f"{member} got banned in the ass")
    except AttributeError:
        await ctx.send("must be in a server to use this command",delete_after=2.5)
    except Exception as e:
        await ctx.send(f"no perms or member role too high ({e})",delete_after=2.5)

@client.command()
async def cat(ctx):
    await ctx.message.delete()
    returned = httpx.get("https://api.thecatapi.com/v1/images/search")
    returned = returned.json()
    await ctx.send(returned[0]["url"])

@client.command()
async def dog(ctx):
    await ctx.message.delete()
    returned = httpx.get("https://dog.ceo/api/breeds/image/random")
    returned = returned.json()
    await ctx.send(returned["message"])

@client.command()
async def gif(ctx,*,gif=None):
    global hasgiphy
    global giphyapi
    await ctx.message.delete()
    if hasgiphy:
        giphy_api = giphyapi
        if gif!=None:
            url=f"https://api.giphy.com/v1/gifs/search?api_key={giphy_api}&limit=2&q={gif}"
            r = httpx.get(url)
            #print(r.json()["data"])
            r = r.json()["data"][1]["url"]
            await ctx.send(r)
        else:
            await ctx.send("No gif args!",delete_after=2.5)
    else:
        await ctx.send("No api key!",delete_after=2.5)
@client.command()
async def insult(ctx,member: str):
    await ctx.message.delete()
    try:
        if member!=None:
            us = member
            if us == None:
                us = member
            url = f"https://insult.mattbas.org/api/insult?who={us}"
            r = httpx.get(url)
            await ctx.send(r.text)
        else:
            await ctx.send("No member args!",delete_after=2.5)
    except Exception as e:
        await ctx.send(e,delete_after=2.5)
@client.command()
async def av(ctx,member: discord.Member=None):
    await ctx.message.delete()
    try:
        #await ctx.delete()
        if member!=None:
            await ctx.send(member.avatar_url)
        else:
            await ctx.send(client.user.avatar_url)
    except Exception as e:
        await ctx.send(e,delete_after=2.5)
@client.command()
async def poll(ctx,question,op1,op2):
    await ctx.message.delete()
    if question == None or op1 == None or op2 == None:
        await ctx.send("all args aren't filled!",delete_after=2.5)
    else:
        msg = await ctx.send(f"""
`Poll`

```diff
+{question}
```
1️⃣```yaml
{op1}```
2️⃣ ```yaml
{op2}```

""")
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
@client.command()
async def fucku(ctx,name=None):
    await ctx.message.delete()
    if name!=None:
        #await ctx.send()
        msg = ""
        for i in range(10):
            try:
                url = f"https://insult.mattbas.org/api/insult?who={name}"
                r = httpx.get(url)
                msg = f"{msg}{r.text}\n"
            except Exception as e:
                print("error wtf")
                pass
        await ctx.send(msg)
    else:
        await ctx.send("No member args!",delete_after=2.5)
import random
import string
async def randomchars():
    char = string.ascii_lowercase
    charu = string.ascii_uppercase
    stringgg = ""
    for i in range(8):
        if i%2==0:
            stringgg = f"{stringgg}{random.choice(char)}"
        else:
            stringgg = f"{stringgg}{random.choice(charu)}"
    return stringgg

@client.command()
async def spam(ctx,ammount:int,*,message:str):
    await ctx.message.delete()
    try:
        for i in range(1,ammount+1):
            #await ctx.send(f"{message} | {await randomchars()}")
            await ctx.send(f"{message}")
    except Exception as e:
        await ctx.send(e)

@client.command()
async def ping(ctx):
    await ctx.message.add_reaction("🏓")
@client.command()
async def shutdown(ctx):
    await ctx.message.delete()
    m = await ctx.send("Shutting down...")
    await asyncio.sleep(1)
    await m.edit(content="Succes!")
    await asyncio.sleep(.5)
    await m.delete()
    sys.exit()

@client.command()
async def gay(ctx,*,user=None):
    await ctx.message.delete()
    if user!=None:
        await ctx.send(f"{user} is {random.randint(0,100)}% gay")
    else:
        await ctx.send(f"{ctx.author} is {random.randint(0,100)}% gay")
async def get_joke():
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke()  # Retrieve a random joke
    if joke["type"] == "single":
        delivery = None # Print the joke
        return [joke["joke"],delivery]
    else:
        delivery = joke["delivery"]
        return [joke["setup"],delivery]
@client.command()
async def joke(ctx):
    await ctx.message.delete()
    l = await get_joke()
    joke = l[0]
    delivery = l[1]
    if delivery!=None:
        await ctx.send(joke)
        await asyncio.sleep(2)
        await ctx.send(delivery)
    else:
        await ctx.send(joke)

@client.command()
async def eightball(ctx,*,message:str=None):
    await ctx.message.delete()
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    if message!=None:
        await ctx.send(f"`8ball`\n\nQuestion: {message}\nAnswer: {random.choice(responses)}")
    else:
        await ctx.send("No message!",delete_after=2.5)

@client.command()
async def urban(ctx, *, search_query:str=None):
    await ctx.message.delete()
    try:
        if search_query!=None :
            async with httpx.AsyncClient(http2=True, follow_redirects=True) as client:
                response = await client.get(f'http://api.urbandictionary.com/v0/define?term={search_query}')
            if response.status_code == 200:
                data = response.json()

                if data.get('list'):
                    definition = data['list'][0]['definition']
                    example = data['list'][0]['example']

                    await ctx.send(f'`Urban Dictionary, {search_query} meaning`\n\n**Definition:**\n{definition}\n\n**Example:**\n{example}')
                else:
                    await ctx.send('No results found for that query.',delete_after=2.5)
            else:
                await ctx.send(f'Error fetching data from Urban Dictionary API. Status Code: {response.status_code}',delete_after=2.5)
        else:
            await ctx.send("No word args!",delete_after=2.5)
    except Exception as e:
        print(f'Error fetching Urban Dictionary definition: {e}')
        await ctx.send('Oops! Something went wrong while fetching the definition.',delete_after=2.5)
from io import StringIO
async def executecode(code):
    old = sys.stdout
    redirect=sys.stdout=StringIO()
    exec(code)
    sys.stdout = old
    return redirect.getvalue()
import re
@client.command()
async def run_code(ctx,*,code=None):
    if ctx.author.id == 1054035775206981752:
        try:
            if code!=None:
                code = code.replace("```py","")
                code = code.replace("```","")
                r = await executecode(code)
                print(r)
                await ctx.send(r)
            else:
                await ctx.send("No code given!", delete_after=2.5)
        except Exception as e:
            await ctx.send(e)
@client.command()
async def gpt(ctx,*,prompt=None):
    global hasopenai
    if hasopenai:
        #await ctx.message.delete()
        if prompt!=None:
            await ctx.send(str(get_completion(prompt)))
        else:
            await ctx.send("No prompt provided!",delete_after=2.5)
    else:
        await ctx.send("No openai key!",delete_after=2.5)

@client.command()
async def fact(ctx):
    await ctx.message.delete()
    r = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    #print(r,r.content)
    if r.status_code==200:
        r = r.json()
        r = r['text']
        await ctx.send(f"Here is your fact: {r}")
    else:
        await ctx.send("Failed to fetch fact!",delete_after=2.5)
client.run(token, bot=False)    
