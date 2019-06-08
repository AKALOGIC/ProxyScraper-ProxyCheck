import requests, json
from bs4 import BeautifulSoup as soup 
import os,time

import colorama
from colorama import init,Back,Fore
init()
try:
	os.system("cls")
except:
	os.system("clear")


banner="""__              ____                    __ 
  / /  ___ _    __/ / /__ _    _________ _/ /_
 / _ \/ _ \ |/|/ / / / _ \ |/|/ / __/ _ `/ __/
/_//_/\___/__,__/_/_/\___/__,__/\__/\_,_/\__/                      
 """


a = open("https.txt","r+")
b = open("socks4.txt","r+")
c = open("socks5.txt","r+")

class scrapy():
	
	def get(self):
		url = ("http://proxy-daily.com/")
		req = requests.get(url)
		k = soup(req.text,"lxml")
		proxies = k.find_all("div",{"style":"border-radius:10px;white-space:pre-line;border:solid 3px #ff4c3b;background:#fff;color:#666;padding:4px;width:250px;height:400px;overflow:auto"})
		self.write(proxies)	
	def write(self,proxies):
		print(proxies[0],file=a)
		print(proxies[1],file=b)
		print(proxies[2],file=c)
		
if __name__ == '__main__':
	print(Fore.RED+banner)
	print(Fore.RED+Back.YELLOW)
	print("wait...")
	time.sleep(2)
	scrapy().get()







	
print("EXTRACCION COMPLETA:)")
