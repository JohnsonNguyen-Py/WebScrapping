from bs4 import BeautifulSoup
import requests

url = "https://www.crownandcaliber.com/collections/rolex-daytona-watches"

res = requests.get(url)
docu = BeautifulSoup(res.text, "html.parser")

tag = BeautifulSoup(
    '<span class="override" content="25,100" itemprop="price">25,100</span>').b
tag['itemprop']

pricesOfDaytonas = docu.find_all(text="")
parent = pricesOfDaytonas[0].parent
tagLine = parent.find('')
print(tag)
print(tagLine)

"""
<span class="current-price product-price__price">
<span class="override" content="USD" itemprop="priceCurrency">$</span>
<span class="override" content="25,100" itemprop="price">25,100</span>
</span>
"""
