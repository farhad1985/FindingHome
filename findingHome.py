# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import redis
import requests

r = redis.StrictRedis(host='localhost', port=6379, db=0)
response  = requests.get("https://divar.ir/tehran/تهران/سهروردی-جنوبی/browse/املاک-مسکن/فروش-مسکونی-آپارتمان-خانه-زمین/?v09=1,380000000,420000000&place=8,296")

soup = BeautifulSoup(response.content, "html.parser")

for link in soup.find_all('a'):
    if link.get('class') != None and len(link.get('class')) > 0 :
        if link.get('class')[0] == 'post-card-link':
            r.set(link.get_text(), link.get_text())

keys = r.keys('*')
for key in keys:
    print(key)
