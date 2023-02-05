#CODED BY CHAINIK
#DC:chainik379#0170
#DATE: 4 December 2022
#Whoever steals the code, death will spread its wings on his shoulders MUHAHAHAHAHAHAHA
import sys, subprocess
import colorama
import os 
from colorama import Fore, Style
from pystyle import Colorate, Colors, System, Center, Write, Anime
import datetime
import random 
from random import randint
import requests
#colors:print(Fore.BLACK + 'BLACK')
#print(Fore.BLUE + 'BLUE')
#print(Fore.CYAN + 'CYAN')
#print(Fore.GREEN + 'GREEN')
#print(Fore.LIGHTBLACK_EX + 'LIGHTBLACK_EX')
#print(Fore.LIGHTBLUE_EX + 'LIGHTBLUE_EX')
#print(Fore.LIGHTCYAN_EX + 'LIGHTCYAN_EX')
#print(Fore.LIGHTGREEN_EX + 'LIGHTGREEN_EX')
#print(Fore.LIGHTMAGENTA_EX + 'LIGHTMAGENTA_EX')
#print(Fore.LIGHTRED_EX + 'LIGHTRED_EX')
#print(Fore.LIGHTWHITE_EX + 'LIGHTWHITE_EX')
#print(Fore.LIGHTYELLOW_EX + 'LIGHTYELLOW_EX')
#print(Fore.MAGENTA + 'MAGENTA')
#print(Fore.RED + 'RED')
#print(Fore.RESET + 'RESET')
#print(Fore.WHITE + 'WHITE')
#print(Fore.YELLOW + 'YELLOW')
banner = f'''

  ▄████▄    ██░ ██   ▄▄▄       ██▓  ███▄    █   ██▓  ██ ▄█▀
 ▒██▀ ▀█   ▓██░ ██▒ ▒████▄    ▓██▒  ██ ▀█   █  ▓██▒  ██▄█▒ 
 ▒▓█    ▄  ▒██▀▀██░ ▒██  ▀█▄  ▒██▒ ▓██  ▀█ ██▒ ▒██▒ ▓███▄░ 
 ▒▓▓▄ ▄██▒ ░▓█ ░██  ░██▄▄▄▄██ ░██░ ▓██▒  ▐▌██ ▒░██░ ▓██ █▄ 
 ▒ ▓███▀ ░ ░▓█▒░██▓  ▓█   ▓██▒░██░ ▒██░   ▓██░ ░██░ ▒██▒ █▄
 ░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░▓  ░ ▒░   ▒ ▒ ░▓  ▒ ▒▒ ▓▒
  ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░ ▒ ░░ ░░   ░ ▒░ ▒ ░░ ░▒ ▒░
 ░         ░  ░░ ░  ░   ▒    ▒ ░   ░   ░ ░  ▒ ░░ ░░ ░ 
 ░ ░       ░  ░  ░      ░  ░ ░           ░  ░  ░  ░   
 ░                                                    
 
 '''[1:]


System.Clear()
System.Size(125, 25)
System.Title("ChaiDox")




ban1 = Anime.Fade(Center.Center(banner), Colors.black_to_red,
           Colorate.Vertical, enter=True)



def cls():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')

def Main():
    print(f"{Fore.RED}",banner)
    start = input("                    start?(y/n) ")
    start1 = start.lower()
    if start1 == 'y':
        print()
        print(f"{Fore.BLACK}                       loading...")
        print()
        print()
        print()
        print()
        print()
        nonicnum = str(randint(0,1000))
        today = datetime.datetime.now().strftime('%A, %B %d, %Y')
        nc = input(f"{Fore.RED}"'[!] Nickname: ')
        f = input(f"{Fore.RED}"'[!] Firstname: ')
        ln = input(f"{Fore.RED}"'[!] Lastname: ')
        ag = input(f"{Fore.RED}"'[!] Age: ')
        pn = input(f"{Fore.RED}"'[!] PhoneNumber: ')
        gm = input(f"{Fore.RED}"'[!] Gmail: ')
        ip = input(f"{Fore.RED}"'[!] IP: ')
        cn = input(f"{Fore.RED}"'[!] CountryName: ')
        cc1 = input(f"{Fore.RED}"'[!] CountryCode: ')
        cc = cc1.upper()
        cy = input(f"{Fore.RED}"'[!] City: ')
        pc = input(f"{Fore.RED}"'[!] PostalCode: ')
        la = input(f"{Fore.RED}"'[!] Latitude: ')
        lo = input(f"{Fore.RED}"'[!] Longitude: ')
        sa = input(f"{Fore.RED}"'[!] StreetAdress: ')
        ph = input(f"{Fore.RED}"'[!] Photos(imgur.com): ')
        dt = input(f"{Fore.RED}"'[!] DiscordTag: ')
        fn = input(f"{Fore.RED}"'[!] FatherName: ')
        p = input(f"{Fore.RED}"'[!] PrivateNumber: ')
        mi = input(f"{Fore.RED}"'[!] MoreInfo: ')
        ncc = nc
        if nc=='':
            ncc="NoNickname"+nonicnum
            nc="NoNickname"
        if ln=='':
            ln='NoLastname'
        if f == '':
            f="NoName"
        if ag == '':
            ag="NoAge"  
        if pn == '':
            pn="NoPhoneNumber"
        if gm == '':
            gm="NoGmail"
        if ip == '':
            ip="NoIP"
        if cn == '':
            cn="NoCountryName"
        if cc == '':
            cc="NoCountryCode"
        if cy == '':
            cy="NoCity"
        if pc == '':
            pc="NoPostalCode"
        if la == '':
            la="NoLatitude"
        if lo == '':
            lo="NoLongitude"
        if sa == '':
            sa="NoStreetAdress"
        if ph == '':
            ph="NoPhotos"
        if dt == '':
            dt="NoDiscord"
        if fn == '':
            fn="NoFatherName"
        if p == '':
            p="NoPrivateNumber"
        if mi == '':
            mi="NoMoreInfo"
        inf=f"""
    ·▄▄▄▄        ▐▄• ▄ ▐▄• ▄ ▄▄▄ .·▄▄▄▄  
    ██▪ ██ ▪      █▌█▌▪ █▌█▌▪▀▄.▀·██▪ ██ 
    ▐█· ▐█▌ ▄█▀▄  ·██·  ·██· ▐▀▀▪▄▐█· ▐█▌
    ██. ██ ▐█▌.▐▌▪▐█·█▌▪▐█·█▌▐█▄▄▌██. ██ 
    ▀▀▀▀▀•  ▀█▄▀▪•▀▀ ▀▀•▀▀ ▀▀ ▀▀▀ ▀▀▀▀▀• 
                DoxTool        
                  by
            chainik379#0170 

    [+] DoxDate: {today}
    [+] Nickname: {nc}
    [+] Firstname: {f}
    [+] Lastname: {ln}
    [+] Age: {ag}
    [+] PhoneNumber: {pn}
    [+] Gmail: {gm}
    [+] IP: {ip}
    [+] CountryName: {cn}
    [+] CountryCode: {cc}
    [+] City: {cy}
    [+] PostalCode: {pc}
    [+] Latitude: {la}
    [+] Longitude: {lo}
    [+] StreetAdress: {sa}
    [+] Photos(imgur.com): {ph}
    [+] DiscordTag: {dt}
    [+] FatherName: {fn}
    [+] PrivateNumber: {p}
    [+] MoreInfo: {mi}
 
 """
        

        with open(f"{ncc + '(' + ln + '' + f + ')'}.txt","w",encoding='utf-8') as f:
         f.write(inf)

        location = os.getcwd()
        print(f"[X] done! Dox is Saved in {location}")
        input()

    if start1 == "n":
       print(f"{Fore.BLUE}[-] Bye Bye :)")
       input()
Main()