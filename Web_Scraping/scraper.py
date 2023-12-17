import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.flipkart.com/thakorjifashion-women-kurta-pant-dupatta-set/p/itm90c162e74e00f?pid=ETHGSGR465ZHWKSP&lid=LSTETHGSGR465ZHWKSPZ5B9AD&marketplace=FLIPKART&store=clo%2Fcfv%2Fitg%2Ftys&srno=b_1_7&otracker=browse&fm=organic&iid=b4fe272a-6701-48b4-9dcb-a29de710e8ea.ETHGSGR465ZHWKSP.SEARCH&ppt=browse&ppn=browse&ssid=i8mgsy67gg0000001694372816873")
soup = BeautifulSoup(req.content, "lxml")

#res = soup.title
#print(res.get_text())
#print(res.prettify())

#print(soup.get_text())
print(soup.prettify())