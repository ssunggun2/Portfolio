import requests
import pandas as pd

FormData={
        'appType': 'all'
        ,'dateType': 'd'
        ,'date': '20211002'
        ,'startRank': '1'
        ,'endRank': '200'
        }

headers={
    'accept': '*/*'
    # ,'accept-encoding': 'gzip, deflate, br'
    ,'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
    ,'content-length': '60'
    ,'content-type': 'application/x-www-form-urlencoded;charset=UTF-8;'
    ,'cookie': '_ga=GA1.2.457024046.1633439073; _gid=GA1.2.1874389556.1633439073; ASPSESSIONIDQSASRRDQ=LGMGGCOBIOPICHFFIKIMKOAM; _abx__Zf3YGX6VB0Gr7qbMLIU3lw={"firstPartyId":"7a90cce4-9b2e-4cb3-9f08-ce79ab6e6097","lastFirstOpenId":"1633439073530:55d2278a-2929-4a1b-946d-d002eb0dbe85","lastEventLogId":"1633439135689:2899b4e6-dd25-438b-863e-2782e4161053","lastDailyFirstOpenTime":1633439073531,"session":{"sessionId":"21ccd420-a9f1-4398-8072-a990a11454b9","lastUpdate":1633439135680},"userId":null,"userProperty":{"userProperty":[],"snapshot":null}}; _gat=1'
    ,'origin': 'https://www.mobileindex.com'
    ,'qid': 'req99091633439212644'
    ,'referer': 'https://www.mobileindex.com/'
    ,'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"'
    ,'sec-ch-ua-mobile': '?0'
    ,'sec-ch-ua-platform': '"Windows"'
    ,'sec-fetch-dest': 'empty'
    ,'sec-fetch-mode': 'cors'
    ,'sec-fetch-site': 'same-site'
    ,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }


url = 'https://proxy-insight.mobileindex.com/chart/revenue_rank'

response = requests.post(url=url, headers=headers, data=FormData)
print(response)
data= response.json()
# print(data)

title_list=[]
rank_list=[]
google_list=[]
apple_list=[]

date=data['date']
print(date)
for i in range(200):
    rank= data['data'][i]['rank']
    title = data['data'][i]['app_name']
    apple_rank = data['data'][i]['apple_rank']
    google_rank = data['data'][i]['google_rank']
    # print(rank, title, apple_rank, google_rank)

    title_list.append(title)
    rank_list.append(rank)
    apple_list.append(apple_rank)
    google_list.append(google_rank)

    df=pd.DataFrame({'Ranking': rank_list ,'title': title_list, 'apple_rank': apple_list, 'google_rank': google_list})
print(df)
df.to_csv(f'C:/Users/User/Desktop/workspace/Portfolio/DoKeV/game_ranking/{date}_mobile_game_ranking.csv', index=False)
