##########################
# URLLIB
# Naver Webtoon(평점 평균 계산)
# Create by shamantha
##########################

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=662774&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# 네이버웹툰 목록 전부 가지고 오기
# webtoons = soup.find_all("div", attrs={"class":"rating_type"} ) # 리스트 반환
# for webtoon in webtoons:
#    rate = webtoon.find("strong").get_text()
#    print(rate)

webtoons = soup.find_all("div", attrs={"class":"rating_type"} ) # 리스트 반환
for webtoon in webtoons:
   rate = webtoon.strong.get_text()
   print(rate)



    
    




