# avito
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

names = []
prices = []
images = []

for i in range(0, 5):
    page = requests.get("https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre?o=" + str(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    main = soup.find(class_='sc-116g21e-0 cvFkfp')
    articlesString = main.find_all(type='application/ld+json')
    articles = [json.loads(a.string) for a in articlesString]
    names = names + [a['name'] for a in articles]
    prices = prices + [str(a['offers']['price']) + 'DH' for a in articles]
    print('Page ' + str(i + 1) + ' article found ' + str(len(names)))
df = pd.DataFrame({
    'name': names,
    'price': prices
})
df.to_csv('car.csv')
