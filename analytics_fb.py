import pandas as pd
import os
from datetime import datetime
from data_collection import player_dir
import os
from fb_season_calc import *
import xlsxwriter
import ntpath

files = os.listdir(player_dir)

print(files)

class FantasyBasketball:

    def __init__(self, file):
        self.file = file

    def remove_outliers(self):

        stat = self.file
        df = pd.read_csv(stat)

        deviation = df.loc[:, 'MP'].std()

        df2 = df[~(df['MP'] <= deviation)]
        df2 = df2.drop(columns=['Rk'])

        return df2

    def split_positions(self, pos):
        
        df = self.remove_outliers()

        df = df[df['Pos'] == pos]

        return df



adv_analytics = player_dir + '\\' + files[0]
per36 = player_dir + '\\' + files[1]
per100 = player_dir + '\\' + files[2]
perGame = player_dir + '\\' + files[3]


def excel_document(stat):


    doc = os.path.splitext(stat)[0]
    doc = ntpath.basename(doc)

    
    pg_df = FantasyBasketball(stat).split_positions('PG')
    sg_df = FantasyBasketball(stat).split_positions('SG')
    sf_df = FantasyBasketball(stat).split_positions('SF')
    pf_df = FantasyBasketball(stat).split_positions('PF')
    c_df = FantasyBasketball(stat).split_positions('C')

    positions = {'Point Guard': pg_df, 'Shooting Guard': sg_df, 'Small Forward': sf_df, 'Power Forward': pf_df, 'Center': c_df}

    writer = pd.ExcelWriter(doc + '.xlsx', engine='xlsxwriter')

    for pos in positions:

        

        positions[pos] = positions[pos].sort_values(by=['PER'], ascending = False) if doc == 'advanced_analytics' else positions[pos].sort_values(by=['MP'], ascending = False)

        positions[pos].to_excel(writer, sheet_name = pos, index = False)

    writer.save()

excel_document(adv_analytics)
excel_document(per36)
excel_document(per100)
excel_document(perGame)
