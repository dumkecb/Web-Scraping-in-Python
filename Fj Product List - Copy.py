## Install Python
## Install Pip

#
pip install BeautifulSoup4
pip install pandas 

## 
import pandas as pd
import requests
from  bs4 import BeautifulSoup

url = "https://www.fjallraven.us/collections/mens"
r = requests.get(url)

soup = BeautifulSoup(r.content)

product = soup.find_all('h3')
products = {}
for prod in product:
	products[prod.get_text()] = []

products_df = pd.DataFrame(products)
productList = products_df.T


## Get Prices
prices = soup.find_all("p")

priceRaw = {}
for pric in prices:
	try:
		priceRaw[pric.a.previous_sibling] = []
	except:
		pass

priceRaw_df = pd.DataFrame(priceRaw)

trimPrice = {}
for pric2 in priceRaw:		
	trimPrice["".join(pric2.strip() for pric2 in pric2.split("\n"))] = []

trimPrice_df = pd.DataFrame(trimPrice)
price_row = trimPrice_df.T

table = pd.concat([productList, price_row])

table.to_csv('FJ.csv', sep = '')
