import requests
import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

month = input("Month(MM): ")
day = input("Day(DD): ")
year = input("Year(YYYY): ")

date = year + "" + month + "" + day

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("log-level=3")

driver = webdriver.Chrome(options = chrome_options)
webdriver.Chrome(service=Service(ChromeDriverManager().install()))#executable_path='C:/Users/Emily/Desktop/app/chromedriver.exe')
driver.get("https://www.bookmakersreview.com/ncaab/odds/?date="+date+"&g=full-game&m=pointspread")

print("===============================\n\n")


lol = []


all_divs = driver.find_elements(By.CLASS_NAME, "gridContainer-O4ezT")
tbody = None



for x in all_divs:
    h1 = x.find_elements(By.TAG_NAME, "h1")
    h2 = x.find_elements(By.TAG_NAME, "h2")

    if len(h1) > 0:
        if h1[0].text.strip() == "Upcoming Games":
            print("THERE ARE UPCOMING GAMES HERE - USE THIS TABLE")
            tbody = x.find_element(By.TAG_NAME, "tbody")
    else:
        print("NO UPCOMING GAMES - ENTER NEW DATE")

#print(tbody)

i = 0

for row in tbody.find_elements(By.TAG_NAME, "tr"):
    
    if i % 2 == 0:
        team_name = row.find_elements(By.TAG_NAME, "td")[2]
        team_name = team_name.find_element(By.CLASS_NAME, "nameContainer-1G-1I").text.strip()
        if "#" in team_name:
            ranking = team_name.split(" ")[0]
            team_name = team_name[len(ranking)+1:]
            print("THIS TEAM HAS A RANKING WHAT THE DUCK" + ranking)
        spread = row.find_element(By.CLASS_NAME, "books-1PYN_").text.strip()
    else:
        team_name = row.find_elements(By.TAG_NAME, "td")[1]
        team_name = team_name.find_element(By.CLASS_NAME, "nameContainer-1G-1I").text.strip()
        if "#" in team_name:
            ranking = team_name.split(" ")[0]
            team_name = team_name[len(ranking)+1:]
            print("THIS TEAM HAS A RANKING WHAT THE DUCK" + ranking)
        spread = row.find_element(By.CLASS_NAME, "books-1PYN_").text.strip()
        
    spread = spread.split(" ")[0]
    if spread[len(spread)-1] == "½":
        spread = spread[:len(spread)-1] + ".5"
    
    print(team_name)
    #print(spread)
    #if i % 2 == 1:
    #    print("----")
    
    i += 1


    temp_list = []

    temp_list.append(team_name)
    temp_list.append(spread)

    lol.append(temp_list)



df = pd.DataFrame (lol, columns = ['team_names', 'spreads'])
print (df)
df.to_csv("C:/Users/Emily/Desktop/app/spreads.csv", index = False, header = False)




driver.close()