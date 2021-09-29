##########################
# URLLIB
# Naver Webtoon(요일별 웹툰목록 전부 가지고 오기)
# Create by shamantha
##########################

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# 네이버웹툰 목록 전부 가지고 오기
webtoons = soup.find_all("a", attrs={"class":"title"} ) # 리스트 반환
for webtoon in webtoons:
    print(webtoon.text)


