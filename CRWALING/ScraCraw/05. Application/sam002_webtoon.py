##########################
# URLLIB
# Naver Webtoon(페이지 정보를 잘 알경우)
# Create by shamantha
##########################

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# 페이지에 대한 이해가 높을때 사용
print(soup.title)
print(soup.title.get_text())
print(soup.a)                   # soup 객체에서 처음 발견되는 a를 출력
print(soup.a.attrs)             # a element의 속성 정보를 출력
print(soup.a["href"])           # a element의 속성값 정보를 출력
