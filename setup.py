import os
from colorama import Fore, Back, Style

user = os.system("$USER")

if user != "root":
    print("Lütfen Komudun Başına Sudo Koyunuz")
    os.system("apt install nmap")
    os.system("pip3 install -r requirements.txt")
    os.system("python3 PortScanner.py")
else:
    os.system("apt install nmap")
    os.system("pip3 install -r requirements.txt")
    os.system("python3 PortScanner.py")
