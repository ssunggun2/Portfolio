##########################
# URLLIB
# Naver Webtoon(태그정보 리스팅)
# Create by shamantha
##########################

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# a 태그중 text내용과 동일한 a 태그를 가지고 와라
webtoon = soup.find("a", text ="여성전용헬스장 진달래짐-5화: 맨몸운동 등, 허리" )
print(webtoon)

