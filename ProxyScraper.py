import requests, json
from bs4 import BeautifulSoup as soup 
import os,time

url = ("http://proxy-daily.com/")
req = requests.get(url)
find = soup(req.text,"lxml")
proxies = find.find_all("div",{"style":"border-radius:10px;white-space:pre-line;border:solid 3px #ff4c3b;background:#fff;color:#666;padding:4px;width:250px;height:400px;overflow:auto"})
print(proxies,file=open("a.txt","a",encoding="UTF-8"))
change = open("a.txt","r+")
chagE = change.read().replace('[<div style="border-radius:10px;white-space:pre-line;border:solid 3px #ff4c3b;background:#fff;color:#666;padding:4px;width:250px;height:400px;overflow:auto">',"HTTPS PROXIES \n",1)
chaE = chagE.replace('</div>, <div style="border-radius:10px;white-space:pre-line;border:solid 3px #ff4c3b;background:#fff;color:#666;padding:4px;width:250px;height:400px;overflow:auto">',"SOCKS 4 \n",1)
chE = chaE.replace('</div>, <div style="border-radius:10px;white-space:pre-line;border:solid 3px #ff4c3b;background:#fff;color:#666;padding:4px;width:250px;height:400px;overflow:auto">',"SOCKS 5 \n",1)

print(chE,file=open("proxy.txt","a"))
proxies = open("proxy.txt","r+")
change.close()
os.remove("a.txt")
proxy_https = open("https.txt","a+",encoding="UTF-8")
for lines in proxies.readlines():
	a = True
	while  a == True:
		try:
			proxy_https.write(lines)
			if "SOCKS 4" in lines:
				proxy_https.close()
		except:	
			pass
		break
	
print("EXTRACCION COMPLETA:)")
proxies.close()