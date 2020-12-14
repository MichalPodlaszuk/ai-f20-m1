import requests
import pandas as pd
from bs4 import BeautifulSoup

movie_names = [] # here I create lists to store all variables
descriptions = []
release_dates = []
ratings = []
durations = []
genres = []
filming_dates = []
stars1 = []
directors1 = []

top = requests.get('https://www.imdb.com/list/ls091520106/') # here I request from IMDB top 100 to get directors and genre easily
top1 = BeautifulSoup(top.content, 'html.parser')
directors = top1.find_all('p', class_="text-muted text-small")  # here I find lines that include directors
genre = top1.find_all('span', class_="genre") # here I find all the genres
for element in genre:
    genres.append(str(element.get_text()).strip(' \n ')) # here I append all the genres to the list
for element in range(1, 300, 3):
    a = str(directors[element]).split('>') # here I append all the directors to the list
    directors1.append(a[2].rstrip('</a'))

main_page = requests.get('https://www.imdb.com/chart/top/') # here I request from IMDB top 250
main = BeautifulSoup(main_page.content, 'html.parser')
titles = main.find_all('a')
list_titles = list(titles)
proper_elements = list_titles[60:259:2] # here I locate all the lines of html code that contain the 100 links I need
href = []
for d in range(len(proper_elements)):
    c = (str(proper_elements[d])).split() # here I split those lines relatively to whitespaces so the links themselves are easier to locate
    href.append(c[1])
h = []
for f in href:
    g = f.split('"') # here I split the strings that contain links so that I can get to the links
    h.append(g[1])
k = []
for i in h:
    j = str('https://www.imdb.com' + i) # here I create valid links to websites of each movie
    k.append(j)
for l in range(len(k)):
    title = requests.get(k[l])
    title_beautiful = BeautifulSoup(title.content, 'html.parser') # here I iterate through each website to extract the data I need
    movie_name = title_beautiful.find('h1').get_text() # here I extract names of movies
    movie_names.append(((str(movie_name)).split('('))[0])
    description = title_beautiful.find('div', class_="summary_text").get_text() # here I extract description of each movie
    descriptions.append(description.strip('\n '))
    release_date = title_beautiful.find_all('span', class_="attribute") # here I extract lines of code that contain release dates
    try:
        release_date1 = list(release_date)[1]
        a = str(release_date1).split('>') # here I format lines with release dates so that they display release dates only
        release_dates.append(a[1].rstrip('</span'))
    except IndexError:
        release_dates.append('not known')
    rating = title_beautiful.find('span', itemprop="ratingValue").get_text() # here I extract all the ratings
    ratings.append(f'{rating}/10')
    duration = title_beautiful.find('time').get_text() # here I extract all the durations of movies
    durations.append(str(duration.strip()))
    star = title_beautiful.find_all('div', class_="credit_summary_item") #here I extract lines of code that contain stars of each movie
    random_list = []
    for b in star:
        if 'Stars' in str(b):
            random_list.append(str(b))
    idk = random_list[0].split('>')
    stars_i_guess = idk[4::2]
    okay = stars_i_guess[:-3] # in this for loop I extract proper star names
    proper_stars = []
    for g in okay:
        proper_stars.append(g.rstrip('</a'))
    stars1.append(proper_stars)

for i in h:
    try:
        j = str('https://www.imdb.com' + i + 'locations?ref_=tt_dt_dt') # here I request from all the IMDB sites that contain filming dates of all those movies
        filming = requests.get(j)
        filmings = BeautifulSoup(filming.content, 'html.parser')
        filming_date = filmings.find('li', class_="ipl-zebra-list__item").get_text() # here I extract all those filming dates
        filming_dates.append(str(filming_date).strip(' \n '))
    except AttributeError:
        filming_dates.append('not known')
data = {'Description': descriptions, # here I create data frame for all the info
        'Release Date': release_dates,
        'Director Name': directors1,
        'Rating': ratings,
        'Duration': durations,
        'Genre': genres,
        'Stars': stars1,
        'Filming Dates': filming_dates}
labels = movie_names
df = pd.DataFrame(data, index= labels)
pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', df.shape[0]+1) # and here I set up all the options of dataframe display so that all the info are nice and visible
pd.set_option('display.max_colwidth', None)
df.to_csv('C:/Users/ziolo/Documents/GitHub/ai-f20-m1/w2/d10/Top100IMDB.csv') # it takes around 6-7 minutes for code to execute but it works and it gives a nice data frame that we can save or something :)
