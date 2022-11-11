import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("http://www.espn.com/mens-college-basketball/conferences/schedule/_/id/52/date/20230206")
#print(page.status_code)
#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
filepath = 'C:/Users/Emily/Desktop/app/all_matches/'
#print(soup.prettify())

#for table in soup.find_all('table'):
#    print(table.get('class'))
    
    
table = soup.find('table', class_='tablehead')
df = pd.DataFrame(columns=['date', 'home_team', 'away_team'])
date = ""

i = 0

for row in table.find_all('tr'):
    columns = row.find_all('td')




    if row.get('class')[0] == "stathead" and i == 0:
        date = columns[0].text.strip()
        date = date.split(', ')[1]
        
    if row.get('class')[0] == "stathead" and i != 0:
        df.to_csv(filepath + date + ".csv", index=False)
        date = columns[0].text.strip()
        date = date.split(', ')[1]
    


    if (row.get('class')[0] != "stathead" and row.get('class')[0] != "colhead"):
        a = columns[1].find_all('a')
        if len(a) == 2:
            l = [date, a[0].text.strip(), a[1].text.strip()]
            df.loc[len(df.index)] = l
            
            
    if i == len(table.find_all('tr')) - 1:
        df.to_csv(filepath + date + ".csv", index=False)
    
    i += 1
    
    
            
print(df.head())
print(df.tail())
