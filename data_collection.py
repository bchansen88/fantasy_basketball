import pandas as pd
import os
from fburl_db import *
from fb_season_calc import *
import requests
from bs4 import BeautifulSoup, Comment
import re

year = year_calc()
season = season_calc()

here = os.getcwd()
raw_data = here + '\\stats'
player_dir = raw_data + '\\player\\{}'.format(season)
team_dir = raw_data + '\\team\\{}'.format(season)

def directory_check():

    if not os.path.exists(raw_data):
        os.makedirs(stats)

#directory_check()

def stats_collect(url, stat):

    pattern = r'Jr.$'

    url = url.format(year)
    stat = stat + '.csv'

    df = pd.read_html(url)
    df['Player'] = df['Player'].str.replace(r'Jr.', '')

    print(df)
    df.to_csv('test.csv')
    '''
    df = df[0].dropna(axis=0, thresh=4)
    mask = df['Player'].isin(['Player'])
    df = df[~mask]
    '''
    #df.to_csv(stat, index=False)

def team_stats(url, stat):

    stat = stat + '.csv'
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'lxml')
    x = soup.find('div', {'id': 'all_team-stats-per_game'})
    #table = x.find_all('table')

    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    #df = pd.read_table(x)
    print(len(comments))

'''
stats_collect(fb_ppg, player_dir + '\\points_per_game')
stats_collect(fb_min, player_dir + '\\per_36_minutes')
stats_collect(fb_poss, player_dir + '\\per_100_possesions')
stats_collect(fb_adv, player_dir + '\\advanced_analytics')
'''
stats_collect(fb_ppg, 'per_36_minutes')
