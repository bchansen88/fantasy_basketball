import pandas as pd
import requests
import json



x = requests.get('https://www.oddsshark.com/nba/odds')

print(x.text)

