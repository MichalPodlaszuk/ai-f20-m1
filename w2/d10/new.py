import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
df = pd.read_csv('Top100IMDB.csv').to_numpy()
# duration time conversion to minutes
durations = []
ratings = []
def time_conversion():
    for b in range(5, 900, 9):
        a = (str(np.take(df, [b])).strip("'[]")).split()
        try:
            for i in range(2):
                a[i] = a[i].strip('hmin')
            c = int(a[0]) * 60 + int(a[1])
            durations.append(c)
        except IndexError:
            e = int(a[0]) * 60
            durations.append(e)
time_conversion()
def rating():
    for f in range(4, 900, 9):
        g = (str(np.take(df, [f]))).strip("'[10]").strip('/')
        ratings.append(g)
rating()
def filming_time():
    h = str(np.take(df, [8])).strip
    print(h)
filming_time()
