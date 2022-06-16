from bs4 import BeautifulSoup
import selenium
import requests
import html5lib
import pandas as pd
import csv

URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
r = requests.get(URL)

names = []
distance =[]
mass = []
radius = []
luminosity = []

soup = BeautifulSoup(r.text, 'html5lib')
# print(soup.prettify())

table = soup.find('table')
trows = table.find_all('tr')

# print(trows)
temp_rows = []
for i in trows:
    tdata = i.find_all('td')
    txt = [x.text.rstrip() for x in tdata]
    temp_rows.append(txt)
print(temp_rows)

for i in range(1,len(temp_rows)):
    names.append(temp_rows[i][1])
    distance.append(temp_rows[i][3])
    mass.append(temp_rows[i][5])
    radius.append(temp_rows[i][6])
    luminosity.append(temp_rows[i][7])

df = pd.DataFrame(list(zip(names,distance,mass,radius,luminosity)),columns=["names","distance","mass","radius","luminosity"])
df.to_csv('stars.csv')
