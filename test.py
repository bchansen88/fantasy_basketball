import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from html_table_parser import HTMLTableParser
import urllib.request

'''
file = open('testfile.txt','w')

x = requests.get('https://www.rotowire.com/basketball/nba-lineups.php')

results = x.text

soup = BeautifulSoup(results, 'lxml')
#lineup_teams = soup.find_all('div', class_='lineup is-nba')
lineup_teams = soup.find_all('div', class_='lineup__matchup')

print(len(lineup_teams))

file.write(str(lineup_teams))
file.close()
'''


x = requests.get('https://www.teamrankings.com/nba/stat/defensive-efficiency?date=2021-02-18')
results = x.content
soup = BeautifulSoup(results, "lxml")

print(soup)




