##########################
# URLLIB
# Naver Webtoon(웹툰 세부 목록 가지고 오기)
# Create by shamantha
##########################

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=662774&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# 네이버웹툰 목록 전부 가지고 오기
webtoons = soup.find_all("td", attrs={"class":"title"} ) # 리스트 반환
for webtoon in webtoons:
    link = webtoon.a["href"]
    print(webtoon.a.text, "https://comic.naver.com/"+ link)

    
    
    




