import os
from colorama import Fore, Style, Back
from socket import *

os.system("clear")

print(Fore.CYAN+"""
      
      
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                  
                                        GitHub: https://github/xRiseStrqfe
                                        Discord: https://discord.gg/zcsRyFv
      
      
      
      
      
      """)

print(Fore.RED+"[1] Url İle Hedef Belirleme")
print(Fore.WHITE+"[2] IP İle Hedef Belirleme")

def url_trgt():
    os.system("clear")

    print(Fore.YELLOW+"Hedef:",connection)
    print(Fore.LIGHTGREEN_EX+"[1] Açık Port Taraması")
    print(Fore.LIGHTYELLOW_EX+"[2] Açık Port Taraması Ve Versiyon Tesbiti")
    print(Fore.LIGHTMAGENTA_EX+"[3] Firewall Taraması")
    print(Fore.LIGHTRED_EX+"[4] Basit Port Taraması")
    print(Fore.LIGHTWHITE_EX+"[5] Normal Port Taraması (Nmap Taraması İstemeyenlere)")

    selection = input("Hedefinizi Tarayacağınız Seçenek Nedir?------->")

    if selection == "1":
        print(Back.RED+"----------Açık Port Taraması----------")
        os.system("nmap -Pn -sS -n -v --reason --open"+connection)
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        print("A xRiseStrqfe Script")
    elif selection == "2":
        print(Back.GREEN+"----------Açık Port Taraması Ve Versiyon Tesbiti----------")
        os.system("nmap -sS -sV -sC -n -v"+connection)
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        print("A xRiseStrqfe Script")
    elif selection == "3":
        print(Back.BLUE+"----------FireWall Taraması----------")
        os.system("nmap -sA"+connection)
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        print("A xRiseStrqfe Script")
    elif selection == "4":
        print(Back.BLACK+"----------Basit Port Taraması----------")
        os.system("nmap -sV"+connection)
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        print("A xRiseStrqfe Script")
    elif selection == "5":
        print("----------Normal Port Taraması----------")
        if __name__ == '__main__':
                print("taranıyor:",connection)
                for i in range(6555):
                    connectt=socket(AF_INET,SOCK_STREAM)
                    port_tarama=connectt.connect_ex((connection,i))
                if(port_tarama==0):
                    print("Açık port: %d " %(i))
                    connectt.close()
        input("Tarama Sonlandırıldı")

    else:
        os.system("exit")


def ıp_target():
    os.system("clear")

    print(Fore.YELLOW+"Hedef:",target)
    print(Fore.LIGHTGREEN_EX+"[1] Açık Port Taraması")
    print(Fore.LIGHTYELLOW_EX+"[2] Açık Port Taraması Ve Versiyon Tesbiti")
    print(Fore.LIGHTMAGENTA_EX+"[3] Firewall Taraması")
    print(Fore.LIGHTRED_EX+"[4] Basit Port Taraması")
    print(Fore.LIGHTWHITE_EX+"[5] Normal Port Taraması (Nmap Taraması İstemeyenlere)")

    selection = input("Hedefinizi Tarayacağınız Seçenek Nedir?------->")

    if selection == "1":
        print(Back.RED+"----------Açık Port Taraması----------")
        os.system("nmap -Pn -sS -n -v --reason --open"+target)
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        print("A xRiseStrqfe Script")
    elif selection == "2":
        print(Back.GREEN+"----------Açık Port Taraması Ve Versiyon Tesbiti----------")
        os.system("nmap -sS -sV -sC -n -v"+target)
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        print("A xRiseStrqfe Script")
    elif selection == "3":
        print(Back.BLUE+"----------FireWall Taraması----------")
        os.system("nmap -sA"+target)
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        print("A xRiseStrqfe Script")
    elif selection == "4":
        print(Back.BLACK+"----------Basit Port Taraması----------")
        os.system("nmap -sV"+target)
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        print("A xRiseStrqfe Script")
    elif selection == "5":
        print("----------Normal Port Taraması----------")
        if __name__ == '__main__':
                hedef=input("Hedef: ")
                hedef_ip=gethostbyname(hedef)
                print("taranıyor:",connection)
        
                for i in range(6555):
                    connectt=socket(AF_INET,SOCK_STREAM)
                    port_tarama=connectt.connect_ex((connection,i))
                if(port_tarama==0):
                    print("Açık port: %d " %(i))
                    connectt.close()
        input("Tarama Sonlandırıldı")

    else:
        os.system("exit")


target_selection = input("Cevap---->")

if target_selection == "1":
    url_target = input("Url----->")
    connection = gethostbyname(url_target)
    print(Fore.YELLOW+connection) 
    url_trgt()
elif target_selection == "2":
    target = input("IP---->")
    print(Fore.YELLOW+target)
    ıp_target()
else:
    input("Programı Yeniden Başlatın, Bye Bye")
