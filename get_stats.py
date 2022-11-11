import requests
import pandas as pd
import csv
import time
from bs4 import BeautifulSoup



spreads = None
school_names = None
names = []
stats = []

result = []


with open("C:/Users/Emily/Desktop/app/spreads.csv", newline='') as f:
    reader = csv.reader(f)
    spreads = list(reader)
    
    
with open("C:/Users/Emily/Desktop/app/school_names.csv", newline='') as f:
    reader = csv.reader(f)
    school_names = list(reader)


for x in school_names:
    names.append(x[0])

for x in spreads:
    for y in school_names:
        if x[0] == y[0]:
            
            temp = []
            
            link = "https://www.sports-reference.com/cbb/schools/"+y[1]+"/2023-gamelogs-advanced.html"
            
            temp.append([x[0], link])
            stats.append(temp)
            
counter = 0
total_counter = len(stats)
            
for x in stats:

    link = x[0][1]
    
    page = requests.get(link)
    time.sleep(3.2)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    print(page.status_code)
    table = soup.find('tbody')
    #print(link)
    
    temp = None
    
    
    offensive_rating = 0
    defensive_rating = 0
    pace = 0
    free_throw_attempt_rate = 0
    three_point_attempt_rate = 0
    true_shooting_percentage = 0
    total_rebound_percentage = 0
    assist_percentage = 0
    steal_percentage = 0
    block_percentage = 0
    effective_field_goal_percentage = 0
    turnover_percentage = 0
    offensive_rebound_percentage = 0
    free_throws_per_field_goal_attempt = 0
    opp_effective_field_goal_percentage = 0
    opp_turnover_percentage = 0
    defensive_rebound_percentage = 0
    opp_free_throws_per_field_goal_attempt = 0
    
    num_d1_games = 0
    
    
    
    
    
    for row in table.find_all("tr"):
        if not row.has_attr("class"):
            tds = row.find_all("td")
            
            if tds[2].text.strip() in names:
            
            
                if tds[3].text.strip() == "W" or tds[3].text.strip() == "L":
                    print(tds[3].text.strip())
                    print(tds[2].text.strip())
                    #print(x[0][0])
                    
                    num_d1_games += 1
                    print(num_d1_games)
                    
                    offensive_rating += float(tds[6].text.strip())
                    defensive_rating += float(tds[7].text.strip())
                    pace += float(tds[8].text.strip())
                    free_throw_attempt_rate += float(tds[9].text.strip())
                    three_point_attempt_rate += float(tds[10].text.strip())
                    true_shooting_percentage += float(tds[11].text.strip())
                    total_rebound_percentage += float(tds[12].text.strip())
                    assist_percentage += float(tds[13].text.strip())
                    steal_percentage += float(tds[14].text.strip())
                    block_percentage += float(tds[15].text.strip())
                    effective_field_goal_percentage += float(tds[17].text.strip())
                    turnover_percentage += float(tds[18].text.strip())
                    offensive_rebound_percentage += float(tds[19].text.strip())
                    free_throws_per_field_goal_attempt += float(tds[20].text.strip())
                    opp_effective_field_goal_percentage += float(tds[22].text.strip())
                    opp_turnover_percentage += float(tds[23].text.strip())
                    defensive_rebound_percentage += float(tds[24].text.strip())
                    opp_free_throws_per_field_goal_attempt += float(tds[25].text.strip())
                    
    if offensive_rating != 0 and defensive_rating != 0 and pace != 0:    
        temp = [x[0][0], offensive_rating/num_d1_games, defensive_rating/num_d1_games, pace/num_d1_games, free_throw_attempt_rate/num_d1_games, three_point_attempt_rate/num_d1_games,
        true_shooting_percentage/num_d1_games, total_rebound_percentage/num_d1_games, assist_percentage/num_d1_games, steal_percentage/num_d1_games, block_percentage/num_d1_games,
        effective_field_goal_percentage/num_d1_games, turnover_percentage/num_d1_games, offensive_rebound_percentage/num_d1_games, free_throws_per_field_goal_attempt/num_d1_games,
        opp_effective_field_goal_percentage/num_d1_games, opp_turnover_percentage/num_d1_games, defensive_rebound_percentage/num_d1_games, opp_free_throws_per_field_goal_attempt]
    else:
        temp = [x[0][0], offensive_rating, defensive_rating, pace, free_throw_attempt_rate, three_point_attempt_rate,
        true_shooting_percentage, total_rebound_percentage, assist_percentage, steal_percentage, block_percentage,
        effective_field_goal_percentage, turnover_percentage, offensive_rebound_percentage, free_throws_per_field_goal_attempt,
        opp_effective_field_goal_percentage, opp_turnover_percentage, defensive_rebound_percentage, opp_free_throws_per_field_goal_attempt]
        
    result.append(temp)
    counter+=1
    print("("+str(counter)+"/"+str(total_counter)+") Completed")
            
    #print(temp)        
            
    print("----------------------------")
    
df = pd.DataFrame(result, columns = ['team_name', 'offensive_rating', 'defensive_rating', 'pace', 'free_throw_attempt_rate', 'three_point_attempt_rate', 'true_shooting_percentage', 'total_rebound_percentage', 'assist_percentage',
 'steal_percentage', 'block_percentage', 'effective_field_goal_percentage', 'turnover_percentage', 'offensive_rebound_percentage', 'free_throws_per_field_goal_attempt', 'opp_effective_field_goal_percentage',
 'opp_turnover_percentage', 'defensive_rebound_percentage', 'opp_free_throws_per_field_goal_attempt'])
 
print(df)

df.to_csv("C:/Users/Emily/Desktop/app/stats.csv", index = False, header = False)
    
    
    
    
    
    
    