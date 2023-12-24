#im lazy to add proxies (not just bc i dont have any)
import os
import httpx
import uuid
import threading

# ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator | Coin's Tool") (stop skidding off stack, learn os)
# try to keep all the imports to the top of the file, makes easy for people checking the code

os.system("title [Coin's Tools] Nitro Gen")

black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"

os.system("clear || cls")

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
\__| {white}
""")

ratelimit = False

# not gonna bother checking this func because i can already smell where u got it from

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
            print("{}Succesfully generated promo link: {}{}".format(green,link,white))
            ratelimit=False
    elif response.status_code == 429:
        print(f"{red}rate limit{white}")
        ratelimit = True
    else:
        print("failed {} | content: {}".format(response.status_code,response.content))

while True:
    threading.Thread(target=gen).start()    # rate limit is gonna be wild but ok if u want this way
