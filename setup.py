import os
from colorama import Fore, Back, Style

user = os.system("$USER")

if user != root:
    os.system("sudo python3 setup.py")
else:
    os.system("apt install nmap")
    os.system("pip3 install -r requirements.txt")
    os.system("python3 PortScanner.py")
