import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup


spreads = None
school_names = None
#spreads_names = []

works = []
not_work = []

with open("C:/Users/Emily/Desktop/app/spreads.csv", newline='') as f:
    reader = csv.reader(f)
    spreads = list(reader)

with open("C:/Users/Emily/Desktop/app/school_names.csv", newline='') as f:
    reader = csv.reader(f)
    school_names = list(reader)


for x in spreads:
    if x[0] in (item for sublist in school_names for item in sublist):
        #print("COOLIO" + " " + x[0])
        works.append(x[0])
    else:
        print("BADDIO" + " ----------------- " + x[0])    
        not_work.append(x[0])
        
print("##############################")
        
#THIS IS WHERE I WILL MANUALLY CHANGE ALL THE TEAM NAMES THAT DONT WORK  
for i in range(len(spreads)):
    if spreads[i][0] == "Nebraska-Omaha":
        spreads[i][0] = "Omaha"
    if spreads[i][0] == "Citadel":
        spreads[i][0] = "The Citadel"
    if spreads[i][0] == "Saint Mary's":
        spreads[i][0] = "Saint Mary's (CA)"
    if spreads[i][0] == "USC":
        spreads[i][0] = "Southern California"
        
    if spreads[i][0] == "Saint Joseph's (PA)":
        spreads[i][0] = "Saint Joseph's"
    if spreads[i][0] == "Louisiana-Lafayette":
        spreads[i][0] = "Lafayette"
    if spreads[i][0] == "Southern Miss":
        spreads[i][0] = "Southern Mississippi"
    if spreads[i][0] == "SMU":
        spreads[i][0] = "Southern Methodist"
    if spreads[i][0] == "Ole Miss":
        spreads[i][0] = "Mississippi"
    if spreads[i][0] == "UCF":
        spreads[i][0] = "Central Florida"
    if spreads[i][0] == "Bowling Green":
        spreads[i][0] = "Bowling Green State"
    if spreads[i][0] == "Charleston":
        spreads[i][0] = "College of Charleston"
    if spreads[i][0] == "Loyola Chicago":
        spreads[i][0] = "Loyola (IL)"
    if spreads[i][0] == "BYU":
        spreads[i][0] = "Brigham Young"
    if spreads[i][0] == "USC Upstate":
        spreads[i][0] = "South Carolina Upstate"
    if spreads[i][0] == "St. Francis (BKN)":
        spreads[i][0] = "St. Francis (NY)"
    if spreads[i][0] == "Bryant University":
        spreads[i][0] = "Bryant"
    if spreads[i][0] == "North Carolina State":
        spreads[i][0] = "NC State"
    if spreads[i][0] == "Texas A&M-CC":
        spreads[i][0] = "Texas A&M-Corpus Christi"
    if spreads[i][0] == "Grambling State":
        spreads[i][0] = "Grambling"
    if spreads[i][0] == "Southern University":
        spreads[i][0] = "Southern"
    if spreads[i][0] == "N.J.I.T.":
        spreads[i][0] = "NJIT"
                
for x in spreads:
    if x[0] in (item for sublist in school_names for item in sublist):
        works.append(x[0])
    else:
        print("BADDIO" + " ----------------- " + x[0])    
        not_work.append(x[0])           
print("###Changes Have Been Made#####")        


df = pd.DataFrame(spreads, columns = ['team_names', 'spreads'])
print(df)
df.to_csv("C:/Users/Emily/Desktop/app/spreads.csv", index = False, header = False)











    
#----------Making list of names that work or not--------------
df = pd.DataFrame(works, columns = ['school_name'])
dt = pd.DataFrame(not_work, columns = ['school_name'])
df.to_csv("C:/Users/Emily/Desktop/app/yes_works.csv", index = False, header = False)
dt.to_csv("C:/Users/Emily/Desktop/app/not_works.csv", index = False, header = False)
#-------------------------------------------------------------
