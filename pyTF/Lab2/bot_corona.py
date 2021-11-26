import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

page = requests.get("https://www.worldometers.info/coronavirus/#countries")
soup = BeautifulSoup(page.content, 'html.parser')
main = soup.find_all(class_='main_table_countries_div')[1] \
    .find_all(class_='table table-bordered table-hover main_table_countries')[0] \
    .find_all("tbody")[0].find_all(class_="total_row_world row_continent")
print(main)
