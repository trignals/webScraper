import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


url = "https://www.wikipedia.org/"
results = requests.get(url)

soup = BeautifulSoup(results.text, "html.parser")

#initialise data storage lists
language = []
article_count = []

entry_div = soup.find_all('div', class_='central-featured-lang')


for container in entry_div:

    # language
    data = container.attrs.get('lang')
    language.append(data)

    # article_count
    data = container.bdi.text
    data = data.replace('\xa0', '')
    data = data[0: -1]
    article_count.append(data)

if __name__ == '__main__':

    print(language)
    print(article_count)
    #print(entry_div)
    #print(soup.prettify())
