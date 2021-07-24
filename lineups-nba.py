import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import re

file = open('testfile.txt','w')

x = requests.get('https://www.rotowire.com/basketball/nba-lineups.php')

results = x.text

soup = BeautifulSoup(results, 'lxml')
#lineup_teams = soup.find_all('div', class_='lineup is-nba')
lineup_teams = soup.find_all('div', class_='lineup__matchup')

lineup_main = soup.find_all('div', class_='lineup__main')

lineups = []

def matchup_split():

    team_item = {}

    domain, team = a['href'].split('=')
    team_item['Team'] = team
    for record in a.find('span'):
        record = record.strip('()')
        team_item['record'] = record

    return team_item




for matchup in lineup_teams:

    i = 1
    matchup_item = {}

    for a in matchup.find_all('a', href=True):

        if i == 1:

            away = matchup_split()
            matchup_item['Away'] = (away)

        elif i == 2:
            home = matchup_split()
            matchup_item['Home'] = (home)

        i += 1

    lineups.append(matchup_item)

for players in lineup_main:

    print(players)


file.write(str(lineup_teams))
file.close()
