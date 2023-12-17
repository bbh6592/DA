import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=samsung&crid=3XE1M3LVJ90P&sprefix=samsung%2Caps%2C262&ref=nb_sb_noss_1" 

r = requests.get(url, proxies=proxies)

soup = BeautifulSoup(r.text, 'html.parser') 