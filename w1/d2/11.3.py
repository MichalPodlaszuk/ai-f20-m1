import requests
import pandas as pd
from bs4 import BeautifulSoup
main_page = requests.get('https://www.imdb.com/chart/top/')
main = BeautifulSoup(main_page.content, 'html.parser')
titles = main.find_all('a')
list_titles = list(titles)
proper_elements = list_titles[60:259:2]
href = []

test = requests.get('https://www.imdb.com/title/tt0111161/')
test1 = BeautifulSoup(test.content, 'html.parser')
print(test1.find_all('div'))