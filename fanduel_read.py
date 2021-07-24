import pandas as pd
from dfs_utility import *
import os

here = os.getcwd()

fanduel = find_csv_file(here, suffix = '.csv', data = 'FanDuel')

df = pd.read_csv(fanduel)

def fanduel_structure(df):

    df['Salary Goal'] = ((df['Salary'] * 5)/1000).round(1)
    df['FPPG'] = df['FPPG'].round(2)

    df.rename(columns={'Nickname': 'Player', 'Position': 'Pos', 'Opponent': 'Opp'}, inplace=True)
    df = df.reindex(columns=['Player', 'Pos', 'Team', 'Salary', 'Salary Goal', 'FPPG', 'Injury Indicator', 'Opp', 'Game'])

    return df


if __name__ == '__main__':
    x = fanduel_structure(df)
    x.to_csv('salary.csv')
