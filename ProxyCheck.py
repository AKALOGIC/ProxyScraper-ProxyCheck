import requests,os,time,colorama
from colorama import init,Fore,Back
from random import choice
init()
print("""

[01] HTTPS/HTTP
[02] SOCKS4
[03] SOCKS5
	""")
tipo = input("[PANDORACHECK]$")
k = input("DIGA LA RUTA DEL ARCHIVO")
if tipo == "01" or tipo == "1":
	tipo = "http"
if tipo == "02" or tipo == "2":
	tipo = "socks4"
if tipo == "03" or tipo == "3":
	tipo = "socks5"


file = open(k).readlines()
file =[a.rstrip()for a in file]
for lines in file:
	proxies = {"https":tipo +f"://{lines}"}
	try:
		
		a = requests.get("https://canihazip.com/s",proxies=proxies,timeout=3)
		if a.text in lines:
			print(Fore.BLUE + Back.GREEN + "PROXIE LIVE : {}".format(lines))
			print(lines,file=open("proxy_lives.txt","a"))
		else:
			print(Fore.RED+"PROXIE DIE : {}".format(lines))

	except KeyboardInterrupt as e:
		print("saliendo.....")
		break
	except:
		pass
