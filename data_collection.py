import pandas as pd
import os
from fburl_db import *
from fb_season_calc import *

year = year_calc()
season = season_calc()

here = os.getcwd()
raw_data = here + '\\raw_data'
player_dir = raw_data + '\\player\\{}'.format(season)
team_dir = raw_data + '\\team\\{}'.format(season)

def directory_check():

    if not os.path.exists(raw_data):
        os.makedirs(raw_data)
        os.makedirs(player_dir)
        os.makedirs(team_dir)

directory_check()

def stats_collect(url, stat):

    url = url.format(year)
    stat = stat + '.csv'

    df = pd.read_html(url)
    df = df[0].dropna(axis=0, thresh=4)
    mask = df['Player'].isin(['Player'])
    df = df[~mask]
    df.to_csv(stat, index=False)

stats_collect(fb_ppg, player_dir + '\\points_per_game')
stats_collect(fb_min, player_dir + '\\per_36_minutes')
stats_collect(fb_poss, player_dir + '\\per_100_possesions')
stats_collect(fb_adv, player_dir + '\\advanced_analytics')
