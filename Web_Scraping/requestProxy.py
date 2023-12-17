from bs4 import BeautifulSoup
import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

url = "https://www.amazon.in/s?k=samsung&crid=2DGY96040QXAV&sprefix=samsung%2Caps%2C284&ref=nb_sb_noss_1"
r = requests.get(url, proxies=proxies)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())