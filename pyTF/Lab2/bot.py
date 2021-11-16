# avito
import requests
from bs4 import BeautifulSoup
import pandas as pd

names = []
prices = []
images = []

for i in range(0, 30):
    page = requests.get("https://www.avito.ma/fr/maroc/%C3%A0_vendre")
    soup = BeautifulSoup(page.content, 'html.parser')
    main = soup.find(class_='sc-1iznr1b-0 dNVMoJ').find(class_='sc-1gfa0w0-0 sc-1iznr1b-3 bOYeOx gsqEog').find_all(
        class_='sc-1baqrvp-0 cmwijR')
    # [2].find(
    #   class_='sc-1lz4h6h-0 iRSpkV').find(class_='sc-116g21e-0 cvFkfp')
    print(main[0])
    items = main.find_all(class_=("adListCard" + str(i)))
    # print(items)
    prices = prices + [item.find(class_="oan6tk-5 fdibtT").find(class_='sc-1x0vz2r-0 kKGxRt oan6tk-15 caZekr') for item
                       in items]

    print(prices)
