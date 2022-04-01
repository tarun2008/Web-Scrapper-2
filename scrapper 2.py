from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(URL)
soup = bs(page.text,'html.parser')
table = soup.find_all('table')
table_rows = table[7].find_all('tr')
temp_list = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_name = []
distance = []
mass = []
radius = []

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][0])    
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])   

df = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns = ['star_name','distance','mass','radius'])    
print(df)

df.to_csv('dwarf_star.csv')