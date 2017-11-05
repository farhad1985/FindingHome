# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import redis
import requests

r = redis.StrictRedis(host='localhost', port=6379, db=0)
min = 380000000
max = 440000000
response  = requests.get("https://divar.ir/tehran/تهران/سهروردی-جنوبی/browse/املاک-مسکن/فروش-مسکونی-آپارتمان-خانه-زمین/?v09=1,{},{}&place=8,296".format(min, max))

soup = BeautifulSoup(response.content, "html.parser")

def isExist(text):
    item = r.get(text)
    if item == None:
        return False
    return True

print("--- new Item ---")

for link in soup.find_all('a'):
    if link.get('class') != None and len(link.get('class')) > 0 :
        if link.get('class')[0] == 'post-card-link':
            home = link.get_text()
            if isExist(home) == False:
                r.set(home, home)
                print(home)


print("--- old Item ---")
keys = r.keys('*')
for key in keys:
    print(r.get(key))