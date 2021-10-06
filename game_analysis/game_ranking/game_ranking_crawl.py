# from builtins import print
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

date=datetime.today().strftime("%Y-%m-%d")



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}


data = requests.get('https://www.gamemeca.com/ranking.php', headers=headers)
soup = BeautifulSoup(data.text,'html.parser')
# print(soup)


game_name = soup.select('div#main > div#content > div.ranking_list > div.rank-list div.content-left tbody tr')

title_list=[]
for tr in game_name:
    title = tr.select_one('div.game-name a').text
    title_list.append(title)
    
    # print(title_list)

    df=pd.DataFrame({'Title': title_list}, index=None)

df.insert(0, 'Ranking', range(1,51))
print(df)
df.to_csv(f'C:/Users/User/Desktop/workspace/Portfolio/DoKeV/game_ranking/{date}_game_ranking.csv', index=False)
