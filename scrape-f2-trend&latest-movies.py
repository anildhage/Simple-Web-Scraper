import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = 'https://www4.f2movies.to'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#Trending Movies
Movies = []
Year = []
Length = []

for data in soup.findAll("div", attrs={"class": "film-detail film-detail-fix"}):
    name = data.find("h3", attrs={"class": "film-name"})
    year = data.find("span", attrs={"class": "fdi-item"})
    length = data.find("span", attrs={"class": "fdi-item fdi-duration"})
    if not length:
        continue
    Movies.append(name.text.strip())
    Year.append(year.text)
    Length.append(length.text)

print(Movies)
print(Year)
print(Length)

df = pd.DataFrame({'Movies': Movies, 'Year': Year, 'Length': Length} )
df.to_csv('f2-trend-latest.csv', index=True, encoding='utf-8')



