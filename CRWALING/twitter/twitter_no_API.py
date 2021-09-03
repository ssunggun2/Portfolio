import pandas as pd
from twitter_query import getTweetquery

data = pd.read_csv('C:/Users/User/Desktop/workspace/vsc/CRWALING/kpopradar/artist.csv')
name_artist = data.artistsName
name_artist


for i in range(len(name_artist)):
    getTweetquery(f'{name_artist}')