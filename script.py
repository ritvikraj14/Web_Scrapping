import requests
from bs4 import BeautifulSoup
import pandas as pd 
page = requests.get("https://www.carwale.com/marutisuzuki-cars/wagonr10/lxi-2783/")
soup = BeautifulSoup(page.content, 'html.parser')
car1 = soup.find(id="tab-Specs")
desc = [sd.get_text() for sd in car1.select("#specs td")]
print(desc)
