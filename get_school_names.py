import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup


page = requests.get("https://www.sports-reference.com/cbb/seasons/2023-school-stats.html")
#print(page.status_code)
#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
filepath = 'C:/Users/Emily/Desktop/app/all_matches/'
#print(soup.prettify())

#for table in soup.find_all('table'):
#    print(table.get('class'))
    
    
table = soup.find('tbody')
i = 0

result = []

for row in table.find_all('tr'):

    tds = row.find_all('td')
    temp = []
    
    if not row.has_attr("class"):
    
        team_name = tds[0].text.strip()

        a = tds[0].find('a')        
        link = a.get("href")
        
        nickname = link.split("/")[3]
        
        temp = [team_name, nickname]
        result.append(temp)
        
        i += 1

#print(i)

df = pd.DataFrame(result, columns = ['team_name', 'team_nickname'])
print(df)
df.to_csv("C:/Users/Emily/Desktop/app/school_names.csv", index = False, header = False)